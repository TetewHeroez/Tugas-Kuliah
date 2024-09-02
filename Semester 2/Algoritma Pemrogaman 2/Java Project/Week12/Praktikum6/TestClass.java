package 
Week12.Praktikum6;

public class TestClass {
    public static void main(String[] args) {
        BasedOnTime AYCE = new BasedOnTime("AYCE", "Jl. Raya Kuta", "0361-123456", "10.00", "22.00", 60);
        AYCE.InfoRestoran();
        System.out.println("=========================================");
        BasedOnOrder HaiDiLao = new BasedOnOrder("Hai Di Lao", "Jl. Raya Ahmad", "0361-123456", "10.00", "22.00", 2);
        HaiDiLao.InfoRestoran();
        System.out.println("=========================================");
        FastFood KFC = new FastFood("KFC", "Jl. Raya MERR", "0361-123456", "6.00", "24.00");
        KFC.InfoRestoran();
        System.out.println("=========================================");
        OrdinaryFood Suprek = new OrdinaryFood("Suprek", "Jl. Raya Keputih", "0361-123456", "10.00", "22.00");
        Suprek.InfoRestoran();
        System.out.println("=========================================");
    }
}
