package breezycode.springboot_app;

import org.springframework.stereotype.Component;

@Component
public class WelcomeMessage {
    public String sayWelcome() {
        return "\n--- Welcome to Spring Boot! ---\n";
    }   
}