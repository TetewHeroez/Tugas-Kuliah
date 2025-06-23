public class Main2{
  public static void main(String[] args) {
    GeometricObject objek1 = new GeometricObject("merah",true);
    objek1.toString();
    System.out.println(objek1.toString());

    Circle lingkaran_1 = new Circle(3,"biru",true);
    lingkaran_1.printCircle();
  }
}

class GeometricObject{
  private String color;
  private boolean filled;
  private java.util.Date dateCreated;

  public GeometricObject(){
    this.color = "";
    this.filled = false; 
  }

  public GeometricObject(String color, boolean filled){
    this.color = color;
    this.filled = filled;
  }

  public String getColor(){
    return this.color;
  }

  public void setColor(String color){
    this.color = color;
  }

  public boolean isFilled(){
    return this.filled;
  }

  public void setFilled(boolean filled){
    this.filled = filled;
  }

  public java.util.Date getDateCreated(){
    return this.dateCreated;
  }

  public String toString(){
    return "Warna objeknya adalah " + this.color + ", filled? "+this.filled+" Dibuat pada tgl: "+this.dateCreated;
  }
}

class Circle extends GeometricObject{
  private double radius;

  Circle(){
    super();
    this.radius=0;
  }
  Circle(double newRadius){
    super();
    this.radius=newRadius;
  }
  Circle(double newRadius, String color, boolean filled){
    super(color,filled);
    this.radius=newRadius;
  }
  public double getRadius(){
    return this.radius;
  }
  public void setRadius(double radius){
    this.radius = radius;
  }
  public double getArea(){
    return Math.PI*this.radius*this.radius;
  }
  public double getPerimeter(){
    return 2*Math.PI*this.radius;
  }
  public double getDiameter(){
    return 2*this.radius;
  }
  public void printCircle(){
    System.out.println("Lingkaran berjari-jari:"+this.radius);
    System.out.println("Luas lingkaran:"+this.getArea());
    System.out.println("Keliling lingkaran:"+this.getPerimeter());
    System.out.println("Diameter lingkaran:"+this.getDiameter());
    System.out.println("Lingkaran berwarna:"+this.getColor());
    System.out.println("Filled :"+this.isFilled());
  }
}
