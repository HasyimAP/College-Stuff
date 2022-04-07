
class Mahasiswa{
    private int NIM;
    private String nama;

    public Mahasiswa( int NIM, String nama){
        this.nama = nama;
        this.NIM = NIM;
    }

    public void Mahasiswa(String nama){
        this.nama = nama;
    }

    public void Mahasiswa(){
        System.err.println("Nama\t: " + this.nama);
        System.out.println("NIM\t: " + this.NIM);
    }
}

public class Tugas_5 {
    public static void main(String[] args) {
        Mahasiswa mahasiswa1 = new Mahasiswa(1101191095, "Hasyim");
        mahasiswa1.Mahasiswa();
        System.out.println("\n");
        mahasiswa1.Mahasiswa("M. Hasyim Abdillah P.");
        mahasiswa1.Mahasiswa();
    }
}
