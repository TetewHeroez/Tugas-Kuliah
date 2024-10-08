package Week12.Praktikum6;

class Restoran {
    private String Nama;
    private String Alamat;
    private String NoTelp;
    private String JamBuka;
    private String JamTutup;

    public Restoran() {

    }
    public Restoran(String Nama, String Alamat, String NoTelp, String JamBuka, String JamTutup) {
        this.Nama = Nama;
        this.Alamat = Alamat;
        this.NoTelp = NoTelp;
        this.JamBuka = JamBuka;
        this.JamTutup = JamTutup;
    }
    public void InfoRestoran() {
        System.out.println("Nama Restoran\t: " + Nama);
        System.out.println("Alamat Restoran\t: " + Alamat);
        System.out.println("No Telepon Restoran\t: " + NoTelp);
        System.out.println("Jam Buka-Tutup Restoran\t: " + JamBuka + " - " + JamTutup);
    }
}
// bapak
class SelfService extends Restoran {
    private String Service;
    public SelfService() {
        this.Service = "Self";
    }
    public SelfService(String Nama, String Alamat, String NoTelp, String JamBuka, String JamTutup) {
        super(Nama, Alamat, NoTelp, JamBuka, JamTutup);
        this.Service = "Self";
    }
    public void InfoRestoran() {
        super.InfoRestoran();
        System.out.println("Service\t: " + Service);
    }
}

class BasedOnTime extends SelfService {
    private int WaktuMakan;
    public BasedOnTime(String Nama, String Alamat, String NoTelp, String JamBuka, String JamTutup, int WaktuMakan) {
        super(Nama, Alamat, NoTelp, JamBuka, JamTutup);
        this.WaktuMakan = WaktuMakan;
    }
    public void InfoRestoran() {
        super.InfoRestoran();
        System.out.println("Waktu Makan\t: " + WaktuMakan + " menit");
    }
}
class BasedOnOrder extends SelfService {
    private int Porsi;
    public BasedOnOrder(String Nama, String Alamat, String NoTelp, String JamBuka, String JamTutup, int Porsi) {
        super(Nama, Alamat, NoTelp, JamBuka, JamTutup);
        this.Porsi = Porsi;
    }
    public void InfoRestoran() {
        super.InfoRestoran();
        System.out.println("Waktu Makan\t: " + Porsi + " porsi");
    }
}
// bapak
class RegularService extends Restoran {
    private String Service;
    public RegularService() {
        this.Service = "Regular";
    }
    public RegularService(String Nama, String Alamat, String NoTelp, String JamBuka, String JamTutup) {
        super(Nama, Alamat, NoTelp, JamBuka, JamTutup);
        this.Service = "Regular";
    }
    public void InfoRestoran() {
        super.InfoRestoran();
        System.out.println("Service\t: " + Service);
    }
}

class FastFood extends RegularService {
    private String WaktuSaji;
    public FastFood(String Nama, String Alamat, String NoTelp, String JamBuka, String JamTutup) {
        super(Nama, Alamat, NoTelp, JamBuka, JamTutup);
        this.WaktuSaji = "<5 menit";
    }
    public void InfoRestoran() {
        super.InfoRestoran();
        System.out.println("Waktu Saji\t: " + WaktuSaji);
    }
}
class OrdinaryFood extends RegularService {
    private String WaktuSaji;
    public OrdinaryFood(String Nama, String Alamat, String NoTelp, String JamBuka, String JamTutup) {
        super(Nama, Alamat, NoTelp, JamBuka, JamTutup);
        this.WaktuSaji = ">5 menit";
    }
    public void InfoRestoran() {
        super.InfoRestoran();
        System.out.println("Waktu Saji\t: " + WaktuSaji);
    }
}