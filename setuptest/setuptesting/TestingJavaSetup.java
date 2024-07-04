package setuptest.setuptesting;

import java.util.NoSuchElementException;
import java.util.Scanner;

class TestingJavaSetup {
    public static void main(String[] args) {
        System.out.println("Hello World!");

        Scanner scanner = new Scanner(System.in);
        String nextInp;

        try {
            while (true) {
                nextInp = scanner.nextLine();
                System.out.println(nextInp);
            }
        } catch (NoSuchElementException ex) {
            System.out.println("Printed the file.");
        }

        scanner.close();
    }
}
