package 
Week12.Titik_Garis;

public class cTitik {
    private int x, y;
    public cTitik() {
        this.x = 0;
        this.y = 0;
    }
    public cTitik(int x, int y) {
        this.x = x;
        this.y = y;
    }
    public void setTitik(int x, int y) {
        this.x = x;
        this.y = y;
    }
    public int getX() {
        return x;
    }
    public int getY() {
        return y;
    }
    public cTitik geTitik() {
        return this;
    }
    public String Kuadran() {
        if (x > 0 && y > 0) {
            return "Kuadran I";
        } else if (x < 0 && y > 0) {
            return "Kuadran II";
        } else if (x < 0 && y < 0) {
            return "Kuadran III";
        } else if (x > 0 && y < 0) {
            return "Kuadran IV";
        } else if (x == 0 && y != 0) {
            return "Sumbu Y";
        } else if (y == 0 && x != 0) {
            return "Sumbu X";
        } else {
            return "Titik Pusat";
        }
    }
    public boolean isSegaris(cTitik t1, cTitik t2) {
        cGaris gradien1 = new cGaris(this, t1);
        cGaris gradien2 = new cGaris(t1, t2);
        if (gradien1.getGradien() == gradien2.getGradien()){
            return true;
        }
        else {
            return false;
        }
    }
    public void infoTitik() {
        System.out.println("Titik: (" + x + ", " + y + ")");
    }
}
