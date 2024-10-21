package Week14;

import java.util.ArrayList;
import java.util.Random;

public class Liang_Ch11_9 {
    // Create a n-by-n matrix filled with random 0s and 1s
    public static ArrayList<ArrayList<Integer>> rMatrix(int size) {
        Random random = new Random();
        ArrayList<ArrayList<Integer>> list = new ArrayList<>();
        for (int i = 0; i < size; i++) {
            ArrayList<Integer> innerList = new ArrayList<>();
            for (int j = 0; j < size; j++) {
                innerList.add(random.nextInt(2));
            }
            list.add(innerList);
        }
        return list;
    }
    // Return the Row index with the most 1s
    public static ArrayList<ArrayList<Integer>> MaxRowCol(ArrayList<ArrayList<Integer>> list) {
        ArrayList<ArrayList<Integer>> result = new ArrayList<>();
        ArrayList<Integer> maxRow = new ArrayList<>();
        ArrayList<Integer> maxCol = new ArrayList<>();
        int maxR = 0;
        int maxC = 0;
        for (int i = 0; i < list.size(); i++) {
            int sumR = 0;
            int sumC = 0;
            for (int j = 0; j < list.get(i).size(); j++) {
                sumR += list.get(i).get(j);
                sumC += list.get(j).get(i);
            }
            //Check Row
            if (sumR > maxR) {
                maxR = sumR;
                maxRow.clear();
                maxRow.add(i);
            } else if (sumR == maxR) {
                maxRow.add(i);
            }
            //Check Coloumn
            if (sumC > maxC) {
                maxC = sumC;
                maxCol.clear();
                maxCol.add(i);
            } else if (sumC == maxC) {
                maxCol.add(i);
            }
        }
        result.add(maxRow);
        result.add(maxCol);
        return result;
    }
    // Print the matrix
    public static void PrintMatrix(ArrayList<ArrayList<Integer>> list) {
        for (int i = 0; i < list.size(); i++) {
            for (int j = 0; j < list.get(i).size(); j++) {
                System.out.print(list.get(i).get(j));
            }
            System.out.println();
        }
    }
    // ArrayList to String
    public static String PrintArrayList(ArrayList<Integer> list) {
        String result = "";
        for (int i = 0; i < list.size(); i++) {
            if (i == list.size() - 1){
                result += list.get(i);
                break;
            }
            result += list.get(i) + ", ";
        }
        return result;
    }
}
