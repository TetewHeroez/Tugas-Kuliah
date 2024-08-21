package Week15.Abstract;

public class Main {
    public static void main(String[] args) {
        cCircle circle = new cCircle(7, "Merah");
        System.out.println("Luas Lingkaran: " + circle.hitungLuas());
        System.out.println("Keliling Lingkaran: " + circle.hitungKeliling());
        System.out.println("Warna Lingkaran: " + circle.getWarna());

        cRectangle rectangle = new cRectangle(5, 10, "Biru");
        System.out.println("Luas Persegi Panjang: " + rectangle.hitungLuas());
        System.out.println("Keliling Persegi Panjang: " + rectangle.hitungKeliling());
        System.out.println("Warna Persegi Panjang: " + rectangle.getWarna());
    }
}
