package Week4;

public class CombinatoricONMIPA {
    public static void main(String[] args) {
        System.out.println(Soal9(5));
    }
    public static int Soal9(int i){
        int jawaban=0;
        for (int k = 0; k <= i; k++) {
            for (int j = 0; j <= k; j++) {
                jawaban+=Math.pow(-1, k)*C(i,k)*C(k,j);
            }
        }
        return jawaban;
    }


    public static int C(int n, int r){
        int C_n_r=factorial(n)/(factorial(n-r)*factorial(r));
        return C_n_r;
    }
    public static int factorial(int n){
        int factorial= 1;
        for (int i = n; i >= 1; i--) {
            factorial*=i;
        }
        return factorial;
    }
}
