import java.util.Scanner;

class Matrix{
    int jumlahBaris;
    int jumlahKolom;
    double matrix[][];

    //Constructor
    public Matrix(int jumlahBaris, int jumlahKolom){
        this.jumlahBaris = jumlahBaris;
        this.jumlahKolom = jumlahKolom;

        matrix = new double[jumlahBaris][jumlahKolom];
        zero(this);
    }
    //Pembuat matrix dengan isi 0
    public static void zero(Matrix matrix){
        for(int i = 0; i < matrix.jumlahBaris; i++)
		{
			for(int j = 0; j < matrix.jumlahKolom; j++){
				matrix.matrix[i][j] = 0;
			}
		}
    }
    //Pembuat matrix dengan isi sesuai input system
    public void isiMatrix(Scanner thisScan){
        for(int i = 0; i < this.jumlahBaris; i++){
            for(int j = 0; j < this.jumlahKolom ; j++){
                System.out.println("Baris " + (i+1) + " Kolom " + (j+1));
                this.matrix[i][j] = thisScan.nextDouble();
			}
		}
    }
    //perkalian 2 matrix
    public Matrix multiply(Matrix matrixLain){
        return multiply(this, matrixLain);
    }
    public static Matrix multiply(Matrix matrixPertama, Matrix matrixKedua){
        Matrix matrixHasil = null;

        if (matrixPertama.jumlahKolom == matrixKedua.jumlahBaris){
            matrixHasil = new Matrix(matrixPertama.jumlahBaris, matrixKedua.jumlahKolom);
            for (int i = 0; i < matrixPertama.jumlahBaris; i++){
                for (int j = 0; j < matrixKedua.jumlahKolom; j++){
                    for (int k = 0; k < matrixPertama.jumlahKolom; k++){
                        matrixHasil.matrix[i][j] += matrixPertama.matrix[i][k] * matrixKedua.matrix[k][j];
                    }
                }
            }
        }
        return matrixHasil;
    }
    //membaca isi matrix
    public double getNilai(int baris, int kolom){
        double nilaiMatrix = Double.NaN;
        if ((baris >= 0 && baris < jumlahBaris) && (kolom >= 0 && kolom < jumlahKolom)){
            nilaiMatrix = matrix[baris][kolom];
        }
        return nilaiMatrix;
    }
    //print matrix
    public void printMatrix(){
        for (int i = 0; i < this.jumlahBaris; i++){
            String barisMatrix = "";
            for (int j = 0; j < this.jumlahKolom; j++){
                barisMatrix += String.format("%.2f\t", this.getNilai(i, j));
            }
            System.out.println(barisMatrix);
        }
    }
}

public class No_2 {
    public static void main(String[] args) {
        Scanner myScanner = new Scanner(System.in);
        //Jumlah baris & kolom matrix 1
        System.out.println("Matrix 1\nJumlah Baris:");
        int baris = myScanner.nextInt();
        System.out.println("Jumlah Kolom:");
        int kolom = myScanner.nextInt();
        Matrix matrix1 = new Matrix(baris, kolom);
        //Jumlah baris & kolom matrix 2
        System.out.println("Matrix 2\nJumlah Baris:");
        baris = myScanner.nextInt();
        System.out.println("Jumlah Kolom:");
        kolom = myScanner.nextInt();
        Matrix matrix2 = new Matrix(baris, kolom);
        //Isi matrix 1 & 2
        System.out.println("\nIsi Matrix 1");
        matrix1.isiMatrix(myScanner);
        System.out.println("\nIsi Matrix 2");
        matrix2.isiMatrix(myScanner);
        myScanner.close();
        //matrix 3 = matrix 1 x matrix 2
        Matrix matrix3 = matrix1.multiply(matrix2);
        System.out.println("\nMatrix 3:");
        matrix3.printMatrix();
    }
}