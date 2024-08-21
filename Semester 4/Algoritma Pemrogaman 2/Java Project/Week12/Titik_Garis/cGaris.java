package 
Week12.Titik_Garis;

public class cGaris {
    private double panjang;
    private double gradien;

    public cGaris() {
        this.panjang = 0;
        this.gradien = 0;
    }
    public cGaris(cTitik t1, cTitik t2) {
        this.panjang = Math.sqrt(Math.pow(t2.getX() - t1.getX(), 2) + Math.pow(t2.getY() - t1.getY(), 2));
        this.gradien = (double)(t2.getY() - t1.getY()) / (t2.getX() - t1.getX());
    }
    public void setgaris(cTitik t1, cTitik t2) {
        this.panjang = Math.sqrt(Math.pow(t2.getX() - t1.getX(), 2) + Math.pow(t2.getY() - t1.getY(), 2));
        this.gradien = (double)(t2.getY() - t1.getY()) / (t2.getX() - t1.getX());
    }
    public double getPanjang() {
        return panjang;
    }
    public double getGradien() {
        return gradien;
    }
    public double derajatKemringan() {
        return Math.toDegrees(Math.atan(gradien));
    }
    public boolean isTegakLurus(cGaris g) {
        if (gradien * g.getGradien() == -1) {
            return true;
        } else {
            return false;
        }
    }
    public boolean isSejajar(cGaris g) {
        if (gradien == g.getGradien()) {
            return true;
        } else {
            return false;
        }
    }
    public boolean isHorizontal() {
        if (gradien == 0) {
            return true;
        } else {
            return false;
        }
    }
    public boolean isVertikal() {
        if (gradien == Double.POSITIVE_INFINITY) {
            return true;
        } else {
            return false;
        }
    }
    public void infoGaris() {
        System.out.println("Panjang: " + panjang);
        System.out.println("Gradien: " + gradien);
    }
}
