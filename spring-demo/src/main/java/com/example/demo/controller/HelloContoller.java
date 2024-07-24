package com.example.demo.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import com.example.demo.data.HelloResponse;


@RestController
public class HelloContoller {
   @GetMapping("/hello")
   public HelloResponse getMethodName() {
       return new HelloResponse("hello world", 200);
   }
}
