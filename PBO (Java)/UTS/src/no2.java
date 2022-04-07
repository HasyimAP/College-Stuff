public class no2 {
    public static void main(String[] args) {
        double A, B, C, D;
        A = 1; B = 2; C = 3; D = 4;
        if (C%B == 1){
            D = D + C + B;
            C -= D;
        }
        else {
            D = Math.pow(B, C);
            C += D;
        }
        System.out.println("A = "+A+" | B = "+B+" | C = "+C+" | D = "+D);
    }
}
