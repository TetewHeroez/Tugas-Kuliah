package Week15.Abstract;

public class cRectangle extends cBentuk2D{
    private double panjang;
    private double lebar;

    public cRectangle() {
        this.panjang = 0;
        this.lebar = 0;
    }
    public cRectangle(double panjang, double lebar, String warna) {
        super(warna);
        this.panjang = panjang;
        this.lebar = lebar;
    }
    public double hitungLuas() {
        return panjang * lebar;
    }
    public double hitungKeliling() {
        return 2 * (panjang + lebar);
    }
}
