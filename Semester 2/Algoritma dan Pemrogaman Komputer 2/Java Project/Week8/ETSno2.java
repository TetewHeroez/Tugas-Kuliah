package Week8;

public class ETSno2 {
    public static void main(String[] args) {
        int[] arr={67,23,78,12,43,94};
        MinDistance(arr);
    }
    public static void MinDistance(int[] array){
        int min = Math.abs(array[0]-array[1]);
        for (int i = 0; i < array.length; i++) {
            for (int j = 0; j < i; j++) {
                int distance = Math.abs(array[j]-array[i]);
                if (distance<min) {
                    min=distance;
                }
            }
        }
        System.out.println("Jarak terdekat antara dua elemen adalah "+min);
    }//jika lupa syntax nilai mutlak, dapat juga menggunakan definisi nilai mutlak
}
