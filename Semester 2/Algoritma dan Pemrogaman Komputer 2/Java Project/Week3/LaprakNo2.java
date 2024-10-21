package Week3;

public class LaprakNo2 {
    public static void main(String[] args) {
        XNotDividesN(12, 51);
    }
    public static void XNotDividesN(int x , int batas){
        for (int i = 1; i <= batas; i++) {
            if (i % x != 0) {
                System.out.print(i + " ");
            }
        }
    }
}
