package Week3;
import java.util.Scanner;
public class Praktikum1 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("input angka"); 
        int n = input.nextInt();
        int i = 1;
        int hasil=1;
        while (i<=n) {
            hasil*=i;
            i++;
        }
        System.out.println("Hasil Faktorial = "+hasil);
    }
}
