interface AlatMusik {
    public void mainkan();
    public void stelNada();
    public String ambilNama();
}

public class Tugas_8 {
    public static void main(String[] args) {
        Biola biola1 = new Biola("Fiddle");
        Gitar gitar1 = new Gitar("Gibson");
        biola1.stelNada();
        biola1.mainkan();
        gitar1.stelNada();
        gitar1.mainkan();
        System.out.println("");
        Gesek gesek1 = new Gesek();
        Petik petik1 = new Petik();
        gesek1.nama = biola1.nama;
        petik1.nama = gitar1.nama;
        gesek1.stelNada();
        gesek1.mainkan();
        petik1.stelNada();
        petik1.mainkan();
    }
    
}
