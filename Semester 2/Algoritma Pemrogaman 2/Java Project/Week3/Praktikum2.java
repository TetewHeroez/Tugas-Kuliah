package Week3;

import java.util.Scanner;

public class Praktikum2 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Input suku pertama, beda, dan banyaknya suku"); 
        int a = input.nextInt();
        int b = input.nextInt();
        int n = input.nextInt();
        for (int i = 1; i <= n; i++) {
            if (i==n) {
                System.out.print(a);
                break;
            }
            System.out.print(a+", ");
            a+=b;
        }
    }
}
