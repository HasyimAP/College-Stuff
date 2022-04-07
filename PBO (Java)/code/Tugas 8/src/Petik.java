public class Petik implements AlatMusik {
    String nama;
    public void mainkan(){
        System.out.println("Mainkan alat musik petik " + ambilNama());
    }
    public void stelNada(){
        System.out.println("Stel nada pada alat musik petik " + ambilNama());
    }
    public String ambilNama(){
        return nama;
    }
}

class Gitar extends Petik{
    String nama;
    public Gitar(String nama){
        this.nama = "Gitar " + nama;
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