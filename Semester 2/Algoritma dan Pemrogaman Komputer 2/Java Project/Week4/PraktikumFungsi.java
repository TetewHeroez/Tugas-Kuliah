package Week4;

public class PraktikumFungsi {
    public static void main(String[] args) {
	    double a = 3.0324;
	    double b = 0.8065;
	    double c = -20;
	    double d = 20;
		Output(a,b,c,d);
	}
	public static void Output(double a,double b,double c,double d){
	    double i=0.5;
	    double x0=0;
	    double fx=0;
	    boolean ketemu=false;
	    for (double x=c ; x<=d ; x=x+i){
	        if (x==0){continue;}
	        fx=(a*x+b);
	        System.out.print("f("+x+") = ");
	        System.out.printf("%.4f %n",fx);
	        if (a*x+b==b){
	            ketemu=true;
	            x0=x;
	        }
	    } 
	    if (ketemu){System.out.println("Nilai b ditemukan saat x = "+x0);}
	}
}
