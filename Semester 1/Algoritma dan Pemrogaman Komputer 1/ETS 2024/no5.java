import java.util.Scanner;

public class no5 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Masukkan jumlah data yang diinginkan: ");
        int n = input.nextInt();

        double data = 0.0;
        double sum = 0.0;
        double sum_2 = 0; // Jumlahan kuadrat per data 

        // Loop untuk input data
        System.out.println("Masukkan " + n + " buah data:");
        for (int i = 0; i < n; i++) {
            data = input.nextDouble();
            sum += data;
            sum_2 += data*data;
        }
        double mean = sum / n;
        double s = Math.sqrt((sum_2 - (sum*sum)/n) / (n-1));

        // Print hasil
        System.out.println("Mean: " + mean);
        System.out.println("Standar deviasi: " + s);
    }
    
}