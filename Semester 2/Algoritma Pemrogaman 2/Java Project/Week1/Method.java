package Week1;

public class Method {
    public static void main(String[] args) {
        int[] array= {1,2,4};
        System.out.println(mean(array));
    }
    public static double LuasLingkaran(double r){
        double Luas;
        Luas = Math.PI*r*r;
        return Luas;
    }
    public static int max(int x, int y){
        int num;
        if (x<y) {num=y;}
        else{num=x;}
        return num;
    }
    public static double mean(int[] data){
        int hasil=0;
        for(int i=0;i<data.length;i++){
            hasil+=data[i];
        }
        return (double)hasil/data.length;
    }
}
