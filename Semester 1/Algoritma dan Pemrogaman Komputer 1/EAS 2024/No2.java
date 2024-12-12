import java.util.Arrays;

public class No2 {
    public static int[] minMatrix(int[][] matrix){
	    int[] result = new int[matrix.length];
	    for(int i = 0; i < matrix.length; i++){
	        result[i] = minArray(matrix[i]);
	    }
	    return result;
	}

    public static int minArray(int[] arr){
        int minimum = arr[0];
        for(int j = 0; j < arr.length; j++){
            if(arr[j]<minimum) minimum = arr[j];
        }
        return minimum;
    }

    public static void main(String[] args) {
        int[][] matrix = {
            {1, 2, 3},
            {4, 5, 6},
            {7, 8, 9}
        };
        System.out.println(Arrays.toString(minMatrix(matrix)));
    }
}
