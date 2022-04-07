import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;


class Data{
    public static void findData(ArrayList<Integer> data, int cari){
        int n = 0;
        for (int i = 0; i < data.size(); i++){
            if (data.get(i) == cari){
                System.out.println("Ditemukan pada data ke-" + (i+1));
                n += 1;
            }
        }
        if (n == 0){
            System.out.println("Data tidak ditemukan");
        }
    }
}

public class No_1 {
    public static void main(String[] args) {
        Scanner myScan = new Scanner(System.in);
        System.out.println("Masukan jumlah data: ");
        int jumlahData = myScan.nextInt();
        ArrayList<Integer> data = new ArrayList<Integer>();
        for (int i = 0; i < jumlahData; i++){
            System.out.println("Data ke-" + (i+1) + " :");
            int dataValue = myScan.nextInt();
            data.add(dataValue);
        }
        Collections.sort(data);
        System.out.println("Masukan angka yang anda cari: "); 
        int found = myScan.nextInt();
        Data.findData(data, found);
        myScan.close();
    }
}
