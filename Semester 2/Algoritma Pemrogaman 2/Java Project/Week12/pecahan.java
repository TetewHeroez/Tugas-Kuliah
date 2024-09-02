package Week12;

public class pecahan {
    private int a;
    private int b;

    public pecahan(int pembilang, int penyebut){
        this.a=pembilang;
        this.b=penyebut;
    }

    public void display(){
        System.out.println(this.a+"/"+this.b);
    }

    public pecahan tambah(pecahan p){
        pecahan hasil = new pecahan(this.a*p.b+this.b*p.a,this.b*p.b);
        hasil.a = hasil.a/fpb(this.a*p.b+this.b*p.a,this.b*p.b);
        hasil.b = hasil.b/fpb(this.a*p.b+this.b*p.a,this.b*p.b);
        return hasil;
    }

    public static int fpb(int x, int y) {
        if (y == 0) 
            return x;
        else
            return fpb(y, x % y);
    }
}
