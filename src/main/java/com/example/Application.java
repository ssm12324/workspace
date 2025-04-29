package com.example;

public class Application {
    public static void main(String[] args) {
        System.out.println("🌍 Hello, World from sk012-my-app!");
        try {
            Thread.sleep(Long.MAX_VALUE); // 무한 대기
        } catch (InterruptedException e) {
            System.out.println("🛑 Application interrupted!");
        }
    }
}
