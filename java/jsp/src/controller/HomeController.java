package controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annoatation.RequestMapping;

public class HomeController {

    public HomeController(){

    }

    @RequestMapping
    public String showPage(){
        return "main-menu";
    }
    
}
