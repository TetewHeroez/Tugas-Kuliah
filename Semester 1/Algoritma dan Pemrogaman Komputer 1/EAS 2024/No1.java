public class No1 {
    public static int kali(int m, int n) {
        if (n == 0) return 0;
        return m + kali(m, n - 1);
    }
}