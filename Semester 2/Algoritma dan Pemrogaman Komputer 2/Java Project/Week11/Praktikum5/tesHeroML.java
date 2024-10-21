package Week11.Praktikum5;

public class tesHeroML {
    public static void main(String[] args) {
        HeroML Fanny = new HeroML();
        Fanny.setName("Fanny");
        Fanny.setRole("Assasin");
        Fanny.SetLane("Jungler");
        Fanny.SetMatch(177013);
        Fanny.SetWinrate(69.69);
        Fanny.SetMontageSong("DJ Aku Meriang Remix");

        HeroML YiSunShin = new HeroML();
        YiSunShin.setName("Yi Sun Shin");
        YiSunShin.setRole("Assasin/Marksman");
        YiSunShin.SetLane("Jungler");
        YiSunShin.SetMatch(40986);
        YiSunShin.SetWinrate(89.11);
        YiSunShin.SetMontageSong("DJ Break Beat Kopi Lambada Full Bass");

        HeroML Paquito = new HeroML();
        Paquito.setName("Paquito");
        Paquito.setRole("Fighter/Assasin");
        Paquito.SetLane("Explane");
        Paquito.SetMatch(190867);
        Paquito.SetWinrate(75.86);
        Paquito.SetMontageSong("DJ Phonk");

        HeroML Martis = new HeroML();
        Martis.setName("Martis");
        Martis.setRole("Fighter");
        Martis.SetLane("Jungler/Explane");
        Martis.SetMatch(9991);
        Martis.SetWinrate(56.35);
        Martis.SetMontageSong("DJ Paijo");

        System.out.println("=========================================================");
        Fanny.DisplayHero();
        System.out.println("=========================================================");
        YiSunShin.DisplayHero();
        System.out.println("=========================================================");
        Paquito.DisplayHero();
        System.out.println("=========================================================");
        Martis.DisplayHero();
        System.out.println("=========================================================");

    }
}
