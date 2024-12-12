public class No5 {
    public static int indeksElemenMin(int[] nilai){
        int min = nilai[0];
        int indeks = 0;
        for (int i = 1; i < nilai.length; i++) {
            if (nilai[i] < min) {
                min = nilai[i];
                indeks = i;
            }
        }
        return indeks;
    }
}
