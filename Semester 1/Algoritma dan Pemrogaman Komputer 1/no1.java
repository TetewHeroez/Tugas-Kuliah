import java.util.Scanner;

public class no1 {
    public static void main(String[] args) {
        Scanner inp = new Scanner(System.in);

        System.out.print("Masukkan bilangan: ");
        int n = inp.nextInt();

        boolean isPrima = true;

        // Mengecek keterbagian bilangan n dengan bilangan lain selain 1 dan n itu sendiri
        int k = 2;
        while (k<n) {
            if (n % k == 0) {
                isPrima = false;
            }
            k++;
        }

        if (isPrima) {
            System.out.println(n + " adalah bilangan prima.");
        } else {
            System.out.println(n + " bukan bilangan prima.");
        }
    }
    
}
