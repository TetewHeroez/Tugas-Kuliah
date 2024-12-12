
public class No3 {
    public static int HitungVokal(String kalimat){
        kalimat = kalimat.toLowerCase(); //Mengubah kalimat menjadi huruf kecil
        int jumlahVokal = 0;
        for (int i = 0; i < kalimat.length(); i++) {
            char huruf = kalimat.charAt(i);
            if (huruf == 'a' || huruf == 'i' || huruf == 'u' || huruf == 'e' || huruf == 'o')
                jumlahVokal++;
        }
        return jumlahVokal;
    }

    public static void main(String[] args) {
        String kalimat = "Padamu Alpro 1";
        System.out.println("Jumlah huruf vokal pada kalimat \"" + kalimat + "\" adalah " 
        + HitungVokal(kalimat));
    }
}
