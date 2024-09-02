package Week4;

public class Searching {
    public static void main(String[] args) {
        int[] array={5,9,12,15,17,23,27,38,42,54,64,78,90};
        System.out.println(BinarySearch(array,5));
        System.out.println(LinearSearch(array,5));
    }
    public static int LinearSearch(int[] data, int x){
        int mid=0;
        for (int k = 0; k < data.length; k++) {
            if (data[k]==x) {
                mid = k;
                System.out.println("iterasi Linear = "+ k);
                break;
            }
        }
        return mid;
    }

    public static int BinarySearch(int[] data, int x){
        int mid=0;
        int i=0;
        int k=1;
        int j=data.length-1;
        boolean ketemu=false;
        while (!ketemu&&i<=j) {
            mid=(i+j)/2;
            if (data[mid]==x) {
                ketemu=true;
                System.out.println("iterasi Binary = "+ k);
            }
            else{
                if (data[mid]<x) {
                    i=mid+1;
                }
                else{
                    j=mid-1;
                }
                k++;
            }
        }
        return mid;
    }
}
