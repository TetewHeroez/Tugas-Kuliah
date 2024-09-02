package 
Week9.KalkulatorBilanganKompleks;


import java.util.*;

public class BilanganKompleks {
    private double Re;
    private double Im;

    public BilanganKompleks(double real, double imag){
        this.Im=imag;
        this.Re=real;
    }
    public BilanganKompleks addition(BilanganKompleks other){
        double real = this.Re+other.Re;
        double imag = this.Im+other.Im;
        return new BilanganKompleks(real,imag);
    }
    public BilanganKompleks subtraction(BilanganKompleks other){
        double real = this.Re-other.Re;
        double imag = this.Im-other.Im;
        return new BilanganKompleks(real,imag);
    }
    public BilanganKompleks multlipication(BilanganKompleks other){
        double real = (this.Re*other.Re)-(this.Im*other.Im);
        double imag = (this.Re*other.Im)+(other.Re*this.Im);
        return new BilanganKompleks(real,imag);
    }
    public BilanganKompleks quotient(BilanganKompleks other){
        double real = (this.Re*other.Re+other.Im*this.Im)/(other.Re*other.Re+other.Im*other.Im);
        double imag = (this.Im*other.Re-other.Im*this.Re)/(other.Re*other.Re+other.Im*other.Im);
        return new BilanganKompleks(real,imag);
    }
    public double Modulus(){
        double Modulus = Math.round(Math.sqrt(this.Re*this.Re+this.Im*this.Im)*10000.0)/10000.0;
        return Modulus;
    }
    public double Argument(){
        double Argument = Math.round(Math.toDegrees(Math.atan(this.Im/this.Re))*10000.0)/10000.0;
        return Argument;
    }
    public BilanganKompleks Konjugat(){
        double real = this.Re;
        double imag = -this.Im;
        return new BilanganKompleks(real,imag);
    }
    public BilanganKompleks polar(){
        double radius = Modulus();
        double angle = Argument();
        return new BilanganKompleks(radius,angle);
    }
    public BilanganKompleks square(){
        return this.multlipication(this);
    }
    public BilanganKompleks cubic(){
        return this.multlipication(square());
    }
    public ArrayList<BilanganKompleks> squareRoot() {
        ArrayList<BilanganKompleks> roots = new ArrayList<>();
    
        // Calculate the modulus (r) and argument (theta)
        double r = Math.sqrt(Re * Re + Im * Im);
        double theta = Math.atan2(Im, Re);
    
        // Calculate the square roots
        for (int k = 0; k < 2; k++) {
            double rootR = Math.sqrt(r);
            double rootTheta = (theta + 2 * Math.PI * k) / 2;
    
            double real = Math.round(rootR * Math.cos(rootTheta) * 10000.0) / 10000.0;
            double imag = Math.round(rootR * Math.sin(rootTheta) * 10000.0) / 10000.0;
    
            roots.add(new BilanganKompleks(real, imag));
        }
    
        return roots;
    }
    public ArrayList<BilanganKompleks> cubeRoot() {
        ArrayList<BilanganKompleks> roots = new ArrayList<>();
    
        // Calculate the modulus (r) and argument (theta)
        double r = Math.sqrt(Re * Re + Im * Im);
        double theta = Math.atan2(Im, Re);
    
        // Calculate the cube roots
        for (int k = 0; k < 3; k++) {
            double rootR = Math.cbrt(r);
            double rootTheta = (theta + 2 * Math.PI * k) / 3;
    
            double real = Math.round(rootR * Math.cos(rootTheta) * 10000.0) / 10000.0;
            double imag = Math.round(rootR * Math.sin(rootTheta) * 10000.0) / 10000.0;
    
            roots.add(new BilanganKompleks(real, imag));
        }
    
        return roots;
    }
    public void setRe(double changed){
        this.Re = changed;  
    }
    public void setIm(double changed){
        this.Im = changed;  
    }
    public String Display(){
        String num;
        if (this.Im < 0) {
            num = Double.toString(this.Re)+" - "+Double.toString(-this.Im)+" i";
        } else {
            num = Double.toString(this.Re)+" + "+Double.toString(this.Im)+" i";
        }
        return num;
    }
    public String DspPolar(){
        String num = Double.toString(this.Re)+" cis("+Double.toString(this.Im)+")";
        return num;
    }
}

