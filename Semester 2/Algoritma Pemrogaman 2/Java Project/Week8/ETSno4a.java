package Week8;

public class ETSno4a {
    public static void findThreeLargest(int[] arr){
        int n = arr.length;
        int largest1 = Integer.MIN_VALUE;
        int largest2 = Integer.MIN_VALUE;
        int largest3 = Integer.MIN_VALUE;

        for (int i = 0; i < n; i++) {
            int current = arr[i];

            if(current>largest1){
                largest3 = largest2;
                largest2 = largest1;
                largest1 = current;
            } else if (current<largest1 && current>largest2) {
                largest3 = largest2;
                largest2 = current;
            } else if (current<largest2 && current>largest3) {
                largest3 = current;
            }
        }
        System.out.println("Three largest elements;");
        System.out.println(largest1);
        System.out.println(largest2);
        System.out.println(largest3);
    }
    public static void main(String[] args) {
        int[] arr = {6,4,3,1,8,2,5};
        findThreeLargest(arr);
    }
}
