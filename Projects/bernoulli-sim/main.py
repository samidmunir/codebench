import pygame as PG
import sys as SYSTEM
import random

from config import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    FPS,
    BG_COLOR,
    WING_COLOR,
)


from particle import Particle

PG.init()
SCREEN = PG.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
PG.display.set_caption('Bernoulli Lift Simulation')
CLOCK = PG.time.Clock()

# Wing configuration (global state)
flap_angle = 0        # degrees, 0 to 30
slat_offset = 0       # pixels, 0 to 50
spoiler_height = 0    # incremental, 0 to 20

particles = []  # airflow particles
disturbances = []  # localized flow disruptions

# Lift estimation state
upper_velocities = []
lower_velocities = []


def draw_bezier_curve(points, surface, color, width=2, steps=50):
    def bezier(t, p0, p1, p2, p3):
        return (
            (1 - t)**3 * p0[0] + 3 * (1 - t)**2 * t * p1[0] + 3 * (1 - t) * t**2 * p2[0] + t**3 * p3[0],
            (1 - t)**3 * p0[1] + 3 * (1 - t)**2 * t * p1[1] + 3 * (1 - t) * t**2 * p2[1] + t**3 * p3[1]
        )

    curve_points = []
    for i in range(steps + 1):
        t = i / steps
        curve_points.append(bezier(t, *points))

    PG.draw.lines(surface, color, False, curve_points, width)

def draw_wing(surface, flap_angle=0, slat_offset=0, spoiler_height=0):
    center_y = SCREEN_HEIGHT // 2
    left_x = 300 - slat_offset
    right_x = 700
    camber = 50 + flap_angle

    top_points = [
        (left_x, center_y),
        (left_x + 100, center_y - camber),
        (right_x - 100, center_y - (camber + spoiler_height)),
        (right_x, center_y)
    ]

    bottom_points = [
        (left_x, center_y),
        (left_x + 100, center_y + 20),
        (right_x - 100, center_y + 20 + flap_angle // 2),
        (right_x, center_y + flap_angle)
    ]

    draw_bezier_curve(top_points, surface, WING_COLOR, width=2)
    draw_bezier_curve(bottom_points, surface, WING_COLOR, width=2)
    PG.draw.line(surface, WING_COLOR, (right_x, center_y), (left_x, center_y), 2)

def flow_field(pos):
    wing_y = SCREEN_HEIGHT // 2
    influence_zone = 150
    left_x = 300 - slat_offset
    right_x = 700

    vec = PG.math.Vector2(0, 0)

    # Simulate Bernoulli effect
    if left_x < pos.x < right_x:
        dy = pos.y - wing_y
        if abs(dy) < influence_zone:
            direction = -1 if dy < 0 else 1
            strength = (influence_zone - abs(dy)) / influence_zone
            vec.x += strength * 0.5
            vec.y -= strength * 0.3 * direction

    # BLOCK particles going through the wing
    wing_thickness_top = wing_y - (50 + flap_angle + spoiler_height)
    wing_thickness_bottom = wing_y + (30 + flap_angle)

    if left_x < pos.x < right_x and wing_thickness_top < pos.y < wing_thickness_bottom:
        direction = -1 if pos.y < wing_y else 1
        disturbances.append((pos.x, pos.y, 1.0, direction))
        vec.y += 1.0 * direction
        vec.x -= 0.3

    return vec

def velocity_to_color(velocity):
    # Map particle speed to color (low = blue, high = red)
    speed = velocity.length()
    max_speed = 5.0
    ratio = min(speed / max_speed, 1.0)
    red = int(ratio * 255)
    blue = int((1 - ratio) * 255)
    return (red, 50, blue)

def draw_lift_text(surface, lift_estimate):
    font = PG.font.SysFont("arial", 20)
    text = font.render(f"Estimated Lift: {lift_estimate:.2f}", True, (255, 255, 255))
    surface.blit(text, (20, 20))

def main():
    global flap_angle, slat_offset, spoiler_height

    RUNNING = True
    while RUNNING:
        for EVENT in PG.event.get():
            if EVENT.type == PG.QUIT:
                PG.quit()
                SYSTEM.exit()

            elif EVENT.type == PG.KEYDOWN:
                if EVENT.key == PG.K_f:
                    flap_angle = min(flap_angle + 5, 45)
                elif EVENT.key == PG.K_g:
                    flap_angle = max(flap_angle - 5, 0)
                elif EVENT.key == PG.K_s:
                    slat_offset = min(slat_offset + 5, 50)
                elif EVENT.key == PG.K_a:
                    slat_offset = max(slat_offset - 5, 0)
                elif EVENT.key == PG.K_UP:
                    spoiler_height = min(spoiler_height + 2, 50)
                elif EVENT.key == PG.K_DOWN:
                    spoiler_height = max(spoiler_height - 2, 0)

        SCREEN.fill(BG_COLOR)

        # Spawn new particles
        for _ in range(5):
            y = random.randint(100, SCREEN_HEIGHT - 100)
            particles.append(Particle(0, y))

        upper_velocities.clear()
        lower_velocities.clear()

        # Apply turbulence to nearby particles
        for particle in particles:
            for dx, dy, strength, direction in disturbances:
                dist = particle.pos.distance_to(PG.math.Vector2(dx, dy))
                if dist < 30:
                    turbulence = (30 - dist) / 30
                    particle.vel.y += turbulence * 0.2 * direction
                    particle.vel.x += turbulence * 0.1

        # Update and draw particles with color and trail
        for particle in particles[:]:
            particle.update(flow_field)

            # Trail line behind the particle
            prev_pos = particle.pos - particle.vel * 2
            PG.draw.line(SCREEN, (50, 50, 50), (int(prev_pos.x), int(prev_pos.y)), (int(particle.pos.x), int(particle.pos.y)), 1)

            color = velocity_to_color(particle.vel)
            PG.draw.circle(SCREEN, color, (int(particle.pos.x), int(particle.pos.y)), 2)

            # Categorize for lift estimation
            if 300 < particle.pos.x < 700:
                if particle.pos.y < SCREEN_HEIGHT // 2:
                    upper_velocities.append(particle.vel.length())
                else:
                    lower_velocities.append(particle.vel.length())

            if particle.age > particle.max_age or particle.pos.x > SCREEN_WIDTH:
                particles.remove(particle)

        # Draw wing and lift value
        draw_wing(
            SCREEN,
            flap_angle=flap_angle,
            slat_offset=slat_offset,
            spoiler_height=spoiler_height
        )

        # Lift estimation (difference in average velocities)
        if upper_velocities and lower_velocities:
            avg_upper = sum(upper_velocities) / len(upper_velocities)
            avg_lower = sum(lower_velocities) / len(lower_velocities)
            lift = avg_upper - avg_lower
            draw_lift_text(SCREEN, lift)

        disturbances.clear()
        PG.display.flip()
        CLOCK.tick(FPS)

if __name__ == '__main__':
    main()
