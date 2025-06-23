public class Main {
  public static void main(String[] args) {
    System.out.println("Hello");
    Circle L1 = new Circle();
    Circle L2 = new Circle(7);

    System.out.println("Luas lingkaran L1 adalah "+L1.getArea());
    System.out.println("Luas lingkaran L2 adalah "+L2.getArea());

    System.out.println("Keliling lingkaran L1 adalah "+L1.getPerimeter());
    System.out.println("Keliling lingkaran L2 adalah "+L2.getPerimeter());

    L1.setRadius(2);
    L2.setRadius(4);

    System.out.println("==============================");
    System.out.println("Luas lingkaran L1 adalah "+L1.getArea());
    System.out.println("Luas lingkaran L2 adalah "+L2.getArea());

    System.out.println("Keliling lingkaran L1 adalah "+L1.getPerimeter());
    System.out.println("Keliling lingkaran L2 adalah "+L2.getPerimeter());
  }
}

class Circle{
  double radius;

  Circle(){
    this.radius=0;
  }
  Circle(double newRadius){
    this.radius=newRadius;
  }
  double getArea(){
    return Math.PI*this.radius*this.radius;
  }
  double getPerimeter(){
    return 2*Math.PI*this.radius;
  }
  void setRadius(double newRadius){
    this.radius=newRadius;
  }
}
