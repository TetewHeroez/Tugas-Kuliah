package Week8;

public class ETSno5 {
    public static void main(String[] args) {
        String a;
        String[] nama = new String[1];
        try {
            //statment1;
            //b. a=3;
            //d. System.out.println(1/0);
            
            nama[2] = "Linda";

            //statment2;
            //c. System.out.println(1/0);
        } catch (ArithmeticException ex1) {
            System.out.println(ex1);
        } catch (Exception ex2){
            System.out.println(ex2);
        }
        finally {
            System.out.println("bakso");
        }
        System.out.println("rawon");
    }
}
