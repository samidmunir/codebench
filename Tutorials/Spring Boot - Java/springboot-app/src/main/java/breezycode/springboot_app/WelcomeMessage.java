package breezycode.springboot_app;
import org.springframework.stereotype.Component;

@Component
public class WelcomeMessage {
    public String sayWelcome() {
        return "\nWelcome to Spring Boot!\n";
    }   
}