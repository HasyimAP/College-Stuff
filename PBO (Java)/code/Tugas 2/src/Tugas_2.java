import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class Tugas_2 {
    public static void main(String[] args) {
        Scanner myscan = new Scanner(System.in);
        System.out.println("Jumlah Data : ");
        int jumlah = myscan.nextInt();
        ArrayList<Integer> data = new ArrayList<Integer>();
        for (int i = 0; i < jumlah; i++){
            System.out.println("Data ke-"+(i+1));
            int nilai = myscan.nextInt();
            data.add(nilai);
        }
        myscan.close();
        //average
        int total = 0;
        for (int i = 0; i < data.size(); i++){
            total = total + data.get(i);
        }
        float average = total/jumlah;
        Collections.sort(data);
        //max
        int max = Math.max(data.get(0), data.get(data.size()-1));
        //min
        int min = Math.min(data.get(0), data.get(data.size()-1));
        
        System.out.println("Rata-Rata = " + average);
        System.out.println("Nilai Max = " + max);
        System.out.println("Nilai Min = " + min);
    }
}
