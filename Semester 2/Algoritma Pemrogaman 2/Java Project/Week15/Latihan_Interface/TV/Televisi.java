package 
Week15.Latihan_Interface.TV;

public class Televisi implements interfaceChannelTV, InterfaceElektronik{
    private boolean mesin;
    private String merk;
    private boolean listrik;

    public Televisi(String m){
        mesin = false;
        merk = m;
        listrik = true;
    }
    public void On(){
        mesin = true;
        System.out.println("Televisi "+merk+" On");
    }
    public void Off(){
        mesin = false;
        System.out.println("Televisi "+merk+" Off");
    }
    public void PindahChannel(int c){
        System.out.println("Televisi "+merk+" Channel: "+c);
    }
}
