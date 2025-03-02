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
}