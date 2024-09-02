package Week8;

public class ETSno3 {
    public static void main(String[] args) {
        for (int i = 0; i <= 9; i++) {
            System.out.println("sqrt("+i+") = "+findsqrt(i));
        }
    }
    public static int findsqrt(int x){
        int mid=0;
        int start=0;
        int end=x;
        int ans=0;
        while (start<=end) {
            mid = (start+end)/2;
            int square = mid*mid;
            if(square==x){
               return mid; 
            }
            else if (square<x) {
                start=mid+1;
                ans=mid;
            }
            else{
                end=mid-1;
            }
        }
    return ans;
    }
}
