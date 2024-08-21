package Week15.Abstract;

public class cCircle extends cBentuk2D{
    private double radius;

    public cCircle() {
        this.radius = 0;
    }
    public cCircle(double radius, String warna) {
        super(warna);
        this.radius = radius;
    }
    public double hitungLuas() {
        return Math.PI * radius * radius;
    }
    public double hitungKeliling() {
        return 2 * Math.PI * radius;
    }
}
