
package Week14;

import java.util.ArrayList;
import java.util.Scanner;

public class Liang_Ch11_16 {
    public static void main(String[] args) {
        try (Scanner input = new Scanner(System.in)) {
            int number1 = (int) (Math.random() * 10);
            int number2 = (int) (Math.random() * 10);
            int answer;
            ArrayList<Integer> answers = new ArrayList<>();

            System.out.print("What is " + number1 + " + " + number2 + "? ");
            answer = input.nextInt();

            while (answer != number1 + number2) {
                if (answers.contains(answer)) {
                    System.out.println("You already entered " + answer);
                } else {
                    System.out.println("Wrong answer. Try again.");
                    answers.add(answer);
                }
                System.out.print("What is " + number1 + " + " + number2 + "? ");
                answer = input.nextInt();
            }
        }
        System.out.println("You got it!");
    }
}
