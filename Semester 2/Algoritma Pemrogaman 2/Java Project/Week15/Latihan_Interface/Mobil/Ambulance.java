package Week15.Latihan_Interface.Mobil;

public class Ambulance extends MobilNegara{
    public void NyalakanTape(){
        System.out.println("Tape dinyalakan");
    }
    public void NyalakanTV(){
        System.out.println("TV dinyalakan");
    }
    public void NyalakanAC(){
        System.out.println("AC dinyalakan");
    }
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
    public void NyalakanSirine(){
        System.out.println("Sirine dinyalakan");
    }
    public void MatikanSirine(){
        System.out.println("Sirine dimatikan");
    }
    public void GantiSuaraSirine(int jenis){
        if (jenis == 1) {
            System.out.println("Sirine 1");
        }
        else if (jenis == 2) {
            System.out.println("Sirine 2");
        }
        else if (jenis == 3) {
            System.out.println("Sirine 3");
        }
    }
}
