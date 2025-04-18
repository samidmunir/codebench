package munirsami.runnerz.run;

import java.time.LocalDateTime;
import java.time.temporal.ChronoUnit;
import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

import org.springframework.stereotype.Repository;

import jakarta.annotation.PostConstruct;

@Repository
public class RunRepository {
    
    private List<Run> runs = new ArrayList<>();

    List<Run> findAll() {
        return runs;
    }

    Optional<Run> findById(Integer id) {
        return runs.stream()
           .filter(run -> run.id() == id)
           .findFirst();
    }

    void create(Run run) {
        runs.add(run);
    }

    void update(Run run, Integer id) {
        Optional<Run> existingRun = findById(id);
        
        if (existingRun.isPresent()) {
            runs.set(runs.indexOf(existingRun.get()), run);
        }
    }

    void delete(Integer id) {
        runs.removeIf(run -> run.id().equals(id));
    }

    @PostConstruct
    private void init() {
        runs.add(new Run(1, "First Run", LocalDateTime.now(), LocalDateTime.now().plus(30, ChronoUnit.MINUTES), 3, Location.OUTDOOR));
        runs.add(new Run(2, "Second Run", LocalDateTime.now().plusDays(1), LocalDateTime.now().plusMinutes(45), 5, Location.OUTDOOR));
        runs.add(new Run(3, "Indoor Run", LocalDateTime.now().plusDays(2), LocalDateTime.now().plusDays(2).plusMinutes(45), 5, Location.INDOOR));
    }
}