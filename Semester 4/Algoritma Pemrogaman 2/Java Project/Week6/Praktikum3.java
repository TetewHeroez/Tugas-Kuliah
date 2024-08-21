package 
Week6;
import java.io.*;
import java.util.*;

public class Praktikum3 {
    public static void main(String[] args) throws Exception {
        String data22 = "C:\\Users\\teoso\\OneDrive\\Documents\\Java Project\\Aplro2\\Week6\\Tugas3AlproCSV.csv";
        String line = "";
        String Split = ",";
        List<String[]> Data22 = new ArrayList<>();

        try (BufferedReader br = new BufferedReader(new FileReader(data22))) {
            while ((line = br.readLine()) != null) {
            String[] mahasiswa = line.split(Split);
            Data22.add(mahasiswa);
            }
            } catch (IOException e) {
            e.printStackTrace();
            }
        Message(Data22);
    }

    public static void Message(List<String[]> File) {
        Scanner sc = new Scanner(System.in);
        System.out.println("\nSilahkan inputkan angka untuk memilih pilihan berikut");
        System.out.println("1. Data sebelum diurutkan");
        System.out.println("2. Data setelah diurutkan");
        System.out.println("3. Mencari nama mahasiswa dengan NRP");
        System.out.println("0. Akhiri program\n");
        int cmd = sc.nextInt();

        if (cmd==0) {
            System.out.println("Terima kasih:D");
            return;
        }
        else if(cmd==1){
            DataAwal(File);
        }
        else if(cmd==2){
            DataTerurut(File);
        }
        else if(cmd==3){
            Searching(File);
        }
        else{
            System.out.println("Inputan tidak valid");
            Message(File);
        }
    }
    public static void DataAwal(List<String[]> csv){
        List<String[]> File = csv;
        System.out.println("\nData sebelum diurutkan :");

        for (String[] mahasiswa : File) {
            for (String NamaNRP : mahasiswa) {
                System.out.print(NamaNRP + "\t");
                } 
                System.out.println();
            }
        Message(File);
    }

    public static void DataTerurut(List<String[]> csv){
        List<String[]> File = SelectionSort(csv);

        System.out.println("\nData setelah diurutkan :");
        for (String[] mahasiswa : File) {
            for (String NamaNRP : mahasiswa) {
                System.out.print(NamaNRP + "\t");
                } 
                System.out.println();
            }
        Message(File);
    }

    public static void Searching(List<String[]> File){
        List<String[]> FileSort = SelectionSort(File);
        System.out.println("Ketik -1 untuk keluar dari searching method");
        System.out.print("Masukkan NRP:");
        Scanner sc = new Scanner(System.in);
        Long NRP = sc.nextLong();
        System.out.println();
        if (NRP.equals(-1L)) {
            Message(File);
            return;
        }
        int NoAbsen = BinarySearch(FileSort, NRP);
        if (NoAbsen==-1) {
            System.out.println("Nama Mahasiswa tidak ditemukan");
        }
        else{
            for (String Mahasiswa : FileSort.get(NoAbsen)) {
                System.out.print(Mahasiswa + "\t");
                }
        }
        System.out.println("\n");
        Searching(FileSort);
    }

    public static int BinarySearch(List<String[]> FileSort, Long NRP){
        int mid=0;
        int i=0;
        int j=FileSort.size()-1;
        while (i<=j) {
            mid=(i+j)/2;
            Long Nomor = Long.parseLong(FileSort.get(mid)[0]);
            if (Nomor.equals(NRP)) {
                return mid;
            }
            else{
                if (Nomor<NRP) {
                    i=mid+1;
                }
                else{
                    j=mid-1;
                }
            }
        }
        return -1;
    }
    public static List<String[]> SelectionSort(List<String[]> csv){
        List<String[]> File = csv;
        for (int i = 0; i < File.size(); i++) {
            Long NRPmin = Long.parseLong(File.get(i)[0]);
            int index=i;
            for (int j = i; j < File.size(); j++) {
                if (Long.parseLong(File.get(j)[0])<NRPmin) {
                    NRPmin=Long.parseLong(File.get(j)[0]);
                    index=j;
                }
            }
            String[] temp = File.get(i);
            File.set(i,File.get(index));
            File.set(index,temp);
        }
        return File;
    }

}
