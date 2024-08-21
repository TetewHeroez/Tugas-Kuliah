package Week15.Latihan_Interface.Mobil;

public class MobilPribadi extends Mobil{
    public void NyalakanMesin(){
        mesin = true;
        System.out.println("Mesin dinyalakan");
    }
    public void MatikanMesin(){
        mesin = false;
        System.out.println("Mesin dimatikan");
    }
    public void TambahkanGigi(){
        System.out.println("Gigi ditambahkan");
    }
    public void TurunkanGigi(){
        System.out.println("Gigi diturunkan");
    }
    public void Gas(){
        System.out.println("Gas ditekan");
    }
    public void Rem(){
        System.out.println("Rem ditekan");
    }
}
