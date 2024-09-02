package Week12.Titik_Garis;

public class cTestTitikGaris {
    public static void main(String[] args) {
        cTitik titik1 = new cTitik(1, 1);
        cTitik titik2 = new cTitik(-2, 0);
        cTitik titik3 = new cTitik(-3, -3);
        cTitik titik4 = new cTitik(4, -4);

        cTitik titik5 = new cTitik();
        titik5.infoTitik();
        System.out.println(titik5.Kuadran());
        titik5 = titik4.geTitik();

        cGaris garis1 = new cGaris(titik1, titik2);
        cGaris garis2 = new cGaris(titik3, titik4);

        titik1.infoTitik();
        titik2.infoTitik();
        titik3.infoTitik();
        titik4.infoTitik();
        titik5.infoTitik();
        titik4.setTitik(4, 0);
        titik4.infoTitik();
        System.out.println();
        titik1.infoTitik();
        System.out.println(titik1.Kuadran());
        titik2.infoTitik();
        System.out.println(titik2.Kuadran());
        titik3.infoTitik();
        System.out.println(titik3.Kuadran());
        titik4.infoTitik();
        System.out.println(titik4.Kuadran());
        titik5.infoTitik();
        System.out.println(titik5.Kuadran());

        System.out.println(titik1.isSegaris(titik3, titik4));

        garis1.infoGaris();
        garis2.infoGaris();
        System.out.println("Kemiringan garis1: " + garis1.derajatKemringan());
        System.out.println("Kemiringan garis2: " + garis2.derajatKemringan());
        System.out.println("Garis1 tegak lurus dengan garis2: " + garis1.isTegakLurus(garis2));
        System.out.println("Garis1 sejajar dengan garis2: " + garis1.isSejajar(garis2));
        System.out.println("Garis1 horizontal: " + garis1.isHorizontal());
        System.out.println("Garis1 vertikal: " + garis1.isVertikal());
        System.out.println("Garis2 horizontal: " + garis2.isHorizontal());
        System.out.println("Garis2 vertikal: " + garis2.isVertikal());
        garis2.setgaris(titik2, titik4);
        garis2.infoGaris();
        System.out.println("Garis2 horizontal: " + garis2.isHorizontal());
        titik2.setTitik(0, 1);
        titik4.setTitik(0, 3);
        garis2.setgaris(titik2, titik4);
        garis2.infoGaris();
        System.out.println("Garis2 vertikal: " + garis2.isVertikal());
    }
}
