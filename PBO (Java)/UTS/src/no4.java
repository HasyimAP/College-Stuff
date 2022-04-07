
class ini{
    int a,b;
    void anak(){
        String a = "ini isi dari kelas itu";
        System.out.println(a);
    }
    void testanak(){
        int a = 6; int b = 9;
        System.out.println(a+++b++);
    }
}

class itu extends ini{
    void anak(){
        System.out.println("ini isi dari kelas itu");
    }
}

class testUTS1{
    public static void main(String[] args) {
        itu obj = new itu();
        obj.anak();
        obj.testanak();
    }
}

