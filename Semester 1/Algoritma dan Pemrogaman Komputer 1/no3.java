import java.util.Scanner;

public class no3 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Berat Badan Anda (kg): ");
        double weight = scanner.nextDouble();

        System.out.print("Tinggi Badan Anda (m): ");
        double height = scanner.nextDouble();

        double bmi = weight / (height * height);

        String risk = "";

        if (bmi < 18.5) {
            risk = "Rendah (tapi risiko masalah klinis lain meningkat)";
        } else if (bmi >= 18.5 && bmi <= 22.9) {
            risk = "Rata-rata";
        } else if (bmi >= 23.0 && bmi <= 24.9) {
            risk = "Meningkat";
        } else if (bmi >= 25.0 && bmi <= 29.9) {
            risk = "Sedang";
        } else if (bmi >= 30.0) {
            risk = "Berat";
        }

        System.out.println("BMI Anda: " + bmi);
        System.out.println("Risiko Anda: " + risk);
    }
}
