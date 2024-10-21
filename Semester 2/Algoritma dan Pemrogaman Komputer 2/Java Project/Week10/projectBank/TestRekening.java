package 
Week10.projectBank;

public class TestRekening {
    public static void main(String[] args) {
        cRekening rek1 = new cRekening();

        rek1.setNoRek(1234567890);
        rek1.setPemilik("Tetew Heroez");
        rek1.setor(1000);
        rek1.pinfo();

        rek1.tarik(200);
        rek1.pinfo();
    }
}
