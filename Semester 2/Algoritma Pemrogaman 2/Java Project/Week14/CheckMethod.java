package Week14;

import java.util.Scanner;

public class CheckMethod extends Liang_Ch11_15{
    public static void main(String[] args) {
        try (Scanner input = new Scanner(System.in)) {
            System.out.print("Enter the number of the points: ");
            int n = input.nextInt();
            System.out.println("Enter the coordinates of the points: ");
            System.out.println("Total area is: " + AreaPolygon(InputPoints(n)));
        }
    }
}
