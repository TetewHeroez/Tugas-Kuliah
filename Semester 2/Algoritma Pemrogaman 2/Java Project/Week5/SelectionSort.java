package Week5;

import java.util.Arrays;

public class SelectionSort {
    public static void main(String[] args) {
        int[] data = {1,8,5,6,11};
        System.out.println(Arrays.toString(data));
        System.out.println(Arrays.toString(SelectionSort(data)));
    }
    public static int[] SelectionSort(int[] array){
        int min = array[0];
        int index= 0;
        int temp=0;
        for (int i = 0; i < array.length; i++) {
            min=array[i];
            index=i;
            for (int j = i; j < array.length; j++) {
                if (array[j]<min) {
                    min=array[j];
                    index=j;
                }
            }
            temp = array[index];
            array[index] = array[i];
            array[i]=temp;
        }
        return array;
    }
}
