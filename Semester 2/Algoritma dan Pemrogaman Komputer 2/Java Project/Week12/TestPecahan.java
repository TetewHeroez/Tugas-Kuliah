package Week12;

public class TestPecahan {
    public static void main(String[] args) {
        pecahan p1 = new pecahan(3, 5);
        pecahan p2 = new pecahan(2, 5);

        p1.tambah(p2).display();
    }
}
