package myapp;

import org.example.Math;

public class App {

    public String getGreeting() {
        return "Hello World!";
    }

    public static void main(String[] args) {
        System.out.println("this is public main");
        System.out.println(Math.add(10, 20));
    }
}
