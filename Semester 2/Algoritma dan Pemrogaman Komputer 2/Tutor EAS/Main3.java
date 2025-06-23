public class Main3 {
  public static void main(String[] args) {
    EFG efg = new EFG();
    efg.methodOne();
    efg.methodTwo(3);
    efg.methodThree(2);
  }
}

interface ABC {
  void methodOne();
}
interface PQR {
  void methodTwo();
}

abstract class XYZ implements PQR {
  public void methodTwo(int i){
    System.out.println(Math.pow(i, 2));
  }
  abstract void methodThree(int i);
}

class EFG extends XYZ implements ABC{
  public void methodThree(int i){
    System.out.println(Math.pow(i, 3));
  }
  public void methodOne(){
    System.out.println(4.0);
  }
  public void methodTwo(){

  }
}
