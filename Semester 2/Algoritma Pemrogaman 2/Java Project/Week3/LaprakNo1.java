package Week3;

public class LaprakNo1 {
    public static void main(String[] args) {
        Fibonacci(20);
    }
    public static void Fibonacci (int suku){
        int a = 1;
        int b = 1;
        int sum = 0;
        for (int i = 1; i <= suku; i++) {
            sum = a + b;
            System.out.print(a + " ");
            a=b;
            b=sum;
        }
    }
}
