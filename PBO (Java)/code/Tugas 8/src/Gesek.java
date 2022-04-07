public class Gesek implements AlatMusik {
    String nama;
    public void mainkan(){
        System.out.println("Mainkan alat musik gesek " + ambilNama());
    }
    public void stelNada(){
        System.out.println("Stel nada pada alat musik gesek " + ambilNama());
    }
    public String ambilNama(){
        return nama;
    }
}

class Biola extends Gesek{
    String nama;
    public Biola(String nama){
        this.nama = "Biola " + nama;
    }
    public void mainkan(){
        System.out.println("Mainkan alat musik " + ambilNama());
    }
    public void stelNada(){
        System.out.println("Stel nada pada alat musik " + ambilNama());
    }
    public String ambilNama(){
        return this.nama;
    }
}