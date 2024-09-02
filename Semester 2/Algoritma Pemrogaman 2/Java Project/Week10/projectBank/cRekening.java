package Week10.projectBank;

public class cRekening {
    private int noRek;
    private String pemilik;
    private double saldo;

    public cRekening(){
        this.noRek=0;
        this.pemilik="x";
        this.saldo=0.0;
    }

    public void setNoRek(int num){
        this.noRek=num;
    }
    public void setPemilik(String nama){
        this.pemilik=nama;
    }
    public int getNoRek(){
        return this.noRek;
    }
    public String getPemilik(){
        return this.pemilik;
    }
    public double infoSaldo(){
        return this.saldo;
    }
    public void setor(double uang){
        this.saldo+=uang;
    }
    public void tarik(double nominal){
        this.saldo-=nominal;
    }
    public void pinfo(){
        System.out.println("No Rekening : "+getNoRek());
        System.out.println("Nama Pemilik : "+getPemilik());
        System.out.println("Saldo : "+infoSaldo());
    }
}
