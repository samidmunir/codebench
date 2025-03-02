package munirsami.runnerz.run;

import java.time.LocalDateTime;

public record Run(
    Integer id,
    String title,
    LocalDateTime startTime,
    LocalDateTime completedOn,
    Integer miles,
    Location location
) {
    public Run {
        if (!completedOn.isAfter(startTime)) {
            throw new IllegalArgumentException("Completed on must be after start time!");
        }
    }
}