package Week4;

import java.util.Arrays;

public class Sorting {
    public static void BubbleSort(int[] data){
        System.out.println(Arrays.toString(data));
        for (int i = 0; i < data.length-1; i++) {
            for (int j = 0; j < data.length-1-i; j++) {
                if (data[j+1]<data[j]) {
                    int temp= data[j];
                    data[j]=data[j+1];
                    data[j+1]=temp;
                }
            }
        }
        System.out.println(Arrays.toString(data));
    }

    public static void main(String[] args) {
        int[] array = {3,1,2,4};
        BubbleSort(array);
    }
}
