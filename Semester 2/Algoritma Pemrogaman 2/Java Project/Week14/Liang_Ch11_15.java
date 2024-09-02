
package Week14;

import java.util.ArrayList;
import java.util.Scanner;

public class Liang_Ch11_15 {
    public static double DetArea2D(ArrayList<Double> vec1, ArrayList<Double> vec2) {
        return vec1.get(0) * vec2.get(1) - vec1.get(1) * vec2.get(0);
    }
    public static ArrayList<Double> Vector(ArrayList<Double> origin, ArrayList<Double> end) {
        ArrayList<Double> vector = new ArrayList<>();
        vector.add(end.get(0) - origin.get(0));
        vector.add(end.get(1) - origin.get(1));
        return vector;
    }
    public static ArrayList<ArrayList<Double>> InputPoints(int n){
        ArrayList<ArrayList<Double>> points = new ArrayList<>();
        try (Scanner input = new Scanner(System.in)) {
            for (int i = 0; i < n; i++) {
                ArrayList<Double> innerList = new ArrayList<>();
                for (int j = 0; j < 2; j++) {
                    innerList.add(input.nextDouble());
                }
                points.add(innerList);
            }
        }
        return points;
    }
    public static double AreaPolygon(ArrayList<ArrayList<Double>> points) {
        double area = 0;
        for (int i = 1; i < points.size()-1; i++) {
            ArrayList<Double> vec1 = Vector(points.get(0), points.get(i));
            ArrayList<Double> vec2 = Vector(points.get(0), points.get(i + 1));
            area += Math.abs(DetArea2D(vec1, vec2));
        }
        return area / 2;
    }
}
