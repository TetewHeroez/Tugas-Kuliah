import java.util.Scanner;
public class no2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Masukkan bilangan bulat: ");
        int bilangan = (int) Math.abs(scanner.nextInt());

        int jumlahAngkaGanjil = 0;
        int angka;

        while (bilangan != 0) {
            angka = bilangan % 10; // Ambil digit terakhir
            if (angka % 2 != 0) { // Periksa apakah ganjil
                jumlahAngkaGanjil += angka;
            }
            bilangan /= 10; // Hapus digit terakhir
        }

        System.out.println("Jumlah angka ganjil adalah " + jumlahAngkaGanjil);
    }
}
