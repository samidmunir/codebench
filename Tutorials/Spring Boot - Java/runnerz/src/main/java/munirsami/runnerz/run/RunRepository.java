package munirsami.runnerz.run;

import java.time.LocalDateTime;
import java.time.temporal.ChronoUnit;
import java.util.ArrayList;
import java.util.List;

import org.springframework.stereotype.Repository;

import jakarta.annotation.PostConstruct;

@Repository
public class RunRepository {
    
    private List<Run> runs = new ArrayList<>();

    List<Run> findAll() {
        return runs;
    }

    Run findById(Integer id) {
        return runs.stream()
           .filter(run -> run.id() == id)
           .findFirst()
           .get();
    }

    @PostConstruct
    private void init() {
        runs.add(new Run(1, "First Run", LocalDateTime.now(), LocalDateTime.now().plus(30, ChronoUnit.MINUTES), 3, Location.OUTDOOR));
        runs.add(new Run(2, "Second Run", LocalDateTime.now().plusDays(1), LocalDateTime.now().plusMinutes(45), 5, Location.OUTDOOR));
        runs.add(new Run(3, "Indoor Run", LocalDateTime.now().plusDays(2), LocalDateTime.now().plusDays(2).plusMinutes(45), 5, Location.INDOOR));
    }
}