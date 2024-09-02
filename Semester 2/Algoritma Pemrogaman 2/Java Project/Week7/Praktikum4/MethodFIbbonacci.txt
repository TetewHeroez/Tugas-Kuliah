package Aplro2.Week7.Praktikum4;

import java.util.ArrayList;

public class MethodFIbbonacci {
    public static ArrayList<Integer> Fibbonacci(int x){
        ArrayList<Integer> array = new ArrayList<>();
        int a=0;
        int b=1;
        int sum=a+b;
        while (a<=x) {
            array.add(a);
            a=b;
            b=sum;
            sum=a+b;
        }
        return array;
    }
    public static boolean SameNum(int num){
        String strnum = String.valueOf(num);
        for (int i = 0; i < strnum.length()-1; i++) {
            for (int j = i+1; j < strnum.length(); j++) {
                if (strnum.charAt(i)==strnum.charAt(j)) {
                    return true;
                }
            }
        }
        return false;
    }
}
