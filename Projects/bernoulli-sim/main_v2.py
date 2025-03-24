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
flap_angle = 0
slat_offset = 0
spoiler_height = 0

particles = []
disturbances = []
upper_velocities = []
lower_velocities = []
wing_top_curve = []
wing_bottom_curve = []

def bezier(t, p0, p1, p2, p3):
    return (
        (1 - t)**3 * p0[0] + 3 * (1 - t)**2 * t * p1[0] + 3 * (1 - t) * t**2 * p2[0] + t**3 * p3[0],
        (1 - t)**3 * p0[1] + 3 * (1 - t)**2 * t * p1[1] + 3 * (1 - t) * t**2 * p2[1] + t**3 * p3[1]
    )

def draw_bezier_curve(points, surface, color, width=2, steps=50):
    global wing_top_curve, wing_bottom_curve
    curve_points = [PG.math.Vector2(*bezier(i / steps, *points)) for i in range(steps + 1)]
    if points[1][1] < points[0][1]:  # Top curve
        wing_top_curve = curve_points
    else:
        wing_bottom_curve = curve_points
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
    vec = PG.math.Vector2(0.5, 0)
    for curve in [wing_top_curve, wing_bottom_curve]:
        for i in range(len(curve) - 1):
            segment_start = curve[i]
            segment_end = curve[i + 1]
            seg_vec = segment_end - segment_start
            if seg_vec.length() == 0:
                continue
            to_particle = pos - segment_start
            projection = to_particle.dot(seg_vec.normalize())
            closest = segment_start + seg_vec.normalize() * max(0, min(projection, seg_vec.length()))
            dist = pos.distance_to(closest)
            if dist < 20:
                normal = (pos - closest).normalize()
                tangent = PG.math.Vector2(-normal.y, normal.x)
                influence = (20 - dist) / 20
                vec += tangent * 0.8 * influence
                vec += normal * 0.3 * influence
    return vec

def velocity_to_color(velocity):
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
                    flap_angle = min(flap_angle + 10, 60)
                elif EVENT.key == PG.K_g:
                    flap_angle = max(flap_angle - 10, 0)
                elif EVENT.key == PG.K_s:
                    slat_offset = min(slat_offset + 5, 50)
                elif EVENT.key == PG.K_a:
                    slat_offset = max(slat_offset - 5, 0)
                elif EVENT.key == PG.K_UP:
                    spoiler_height = min(spoiler_height + 2, 50)
                elif EVENT.key == PG.K_DOWN:
                    spoiler_height = max(spoiler_height - 2, 0)

        SCREEN.fill(BG_COLOR)

        for _ in range(5):
            y = random.randint(50, SCREEN_HEIGHT - 50)
            particles.append(Particle(0, y))

        upper_velocities.clear()
        lower_velocities.clear()

        for particle in particles:
            particle.update(flow_field)

        for particle in particles[:]:
            prev_pos = particle.pos - particle.vel * 2
            PG.draw.line(SCREEN, (50, 50, 50), (int(prev_pos.x), int(prev_pos.y)), (int(particle.pos.x), int(particle.pos.y)), 1)
            color = velocity_to_color(particle.vel)
            PG.draw.circle(SCREEN, color, (int(particle.pos.x), int(particle.pos.y)), 2)
            if 300 < particle.pos.x < 700:
                if particle.pos.y < SCREEN_HEIGHT // 2:
                    upper_velocities.append(particle.vel.length())
                else:
                    lower_velocities.append(particle.vel.length())
            if particle.age > particle.max_age or particle.pos.x > SCREEN_WIDTH:
                particles.remove(particle)

        draw_wing(SCREEN, flap_angle, slat_offset, spoiler_height)

        if upper_velocities and lower_velocities:
            avg_upper = sum(upper_velocities) / len(upper_velocities)
            avg_lower = sum(lower_velocities) / len(lower_velocities)
            lift = avg_upper - avg_lower
            draw_lift_text(SCREEN, lift)

        PG.display.flip()
        CLOCK.tick(FPS)

if __name__ == '__main__':
    main()
