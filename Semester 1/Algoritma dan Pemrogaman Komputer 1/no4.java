import java.util.Scanner;
public class no4 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
    
        System.out.print("Masukkan bilangan tiga digit: ");
        int number = input.nextInt();
    
        int digit1 = (int)(number / 100);
        int remaining = number % 100;
        int digit3 = (int)(remaining % 10);
    
        if (digit1 == digit3) {
            System.out.println(number + " merupakan palindrom");
        } else {
            System.out.println(number + " bukan merupakan palindrom");
        }
    }
}

