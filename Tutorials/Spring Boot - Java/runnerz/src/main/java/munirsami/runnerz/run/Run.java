package munirsami.runnerz.run;

import java.time.LocalDateTime;

import jakarta.validation.constraints.NotEmpty;
import jakarta.validation.constraints.Positive;

public record Run(
    Integer id,
    @NotEmpty
    String title,
    LocalDateTime startTime,
    LocalDateTime completedOn,
    @Positive
    Integer miles,
    Location location
) {
    public Run {
        if (!(completedOn.isAfter(startTime))) {
            throw new IllegalArgumentException("Completed on must be after start time!");
        }
    }
}