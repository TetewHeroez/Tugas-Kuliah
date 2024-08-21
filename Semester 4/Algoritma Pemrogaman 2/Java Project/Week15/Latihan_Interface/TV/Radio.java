package 
Week15.Latihan_Interface.TV;

public class Radio implements interfaceChannelRadio, InterfaceElektronik{
    private boolean mesin = false;
    private int volume = 0;
    public void On(){
        mesin = true;
        System.out.println("Radio On");
    }
    public void Off(){
        mesin = false;
        System.out.println("Radio Off");
    }
    public void gantiChannel(int c){
        System.out.println("Radio Channel: "+c);
    }
    public void perbesarVolume(int v){
        volume += v;
        System.out.println("Volume: "+volume);
    }
    public void perkecilVolume(int v){
        volume -= v;
        System.out.println("Volume: "+volume);
    }
}
