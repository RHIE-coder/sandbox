package com.example.demo.data;

public class HelloResponse {
    private String message;
    private int code;

    public HelloResponse(String message, int code) {
        this.message = message;
        this.code = code;
    }

    public String getMessage() {
        return this.message;
    }

    public int getCode() {
        return this.code;
    }
}
