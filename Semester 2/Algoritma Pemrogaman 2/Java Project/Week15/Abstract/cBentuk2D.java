package Week15.Abstract;

public abstract class cBentuk2D {
    private String warna;

    public cBentuk2D() {
        warna = "Transparan";
    }
    public cBentuk2D(String warna) {
        this.warna = warna;
    }

    public void setWarna(String warna) {
        this.warna = warna;
    }
    public String getWarna() {
        return warna;
    }
    
    public abstract double hitungLuas();
    public abstract double hitungKeliling();
}
