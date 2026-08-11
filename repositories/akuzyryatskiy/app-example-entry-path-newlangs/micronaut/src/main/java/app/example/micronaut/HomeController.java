package app.example.micronaut;

import io.micronaut.http.MediaType;
import io.micronaut.http.annotation.Controller;
import io.micronaut.http.annotation.Get;

@Controller("/")
public class HomeController {

    @Get(produces = MediaType.TEXT_HTML)
    public String index() {
        return "<h1>TimeWeb + Micronaut = ❤️</h1>";
    }
}
