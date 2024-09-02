package Week11.Praktikum5;

public class HeroML {
    private String name;
    private String role;
    private String lane;
    private double winrate;
    private int match;
    private String montagesong;

    public HeroML(){
        this.name="-";
        this.role="-";
        this.lane="-";
        this.montagesong="-";
        this.winrate=0.0;
        this.match=0;
    }

    public void setName(String name){
        this.name=name;
    }
    public void setRole(String role){
        this.role=role;
    }
    public void SetLane(String lane){
        this.lane=lane;
    }
    public void SetWinrate(double winrate){
        this.winrate=winrate;
    }
    public void SetMatch(int match){
        this.match=match;
    }
    public void SetMontageSong(String montagesong){
        this.montagesong=montagesong;
    }      

    public void DisplayHero(){
        System.out.println("Hero\t: "+this.name);
        System.out.println("Role\t: "+this.role);
        System.out.println("Lane\t: "+this.lane);
        System.out.println(this.match+" match, winrate: "+this.winrate);
        System.out.println("Montage song: "+this.montagesong);
    }
}
