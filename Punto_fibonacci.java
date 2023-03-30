import java.util.Scanner;
public class Punto_fibonacci{ 
    public static void main(String []args){ 
        Scanner objeto = new Scanner(System.in);
        int x = 0, z = 1, c, w; 
        
        System.out.print("digite un termino de la secuencia de fibonacci");
        w= objeto.nextInt();
        
        for (int i= 0; i<w; i++){ 
            System.out.print(x + ",");
            c= x + z;
            x = z;
            z = c;
        }
        
    }
}
