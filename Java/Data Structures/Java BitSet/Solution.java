import java.io.*;
import java.util.*;

public class Java
{
    public static void main(String [] args)
    {
        Scanner cin = new Scanner(System.in);

        int N = cin.nextInt();
        int M = cin.nextInt();

        BitSet B1 = new BitSet(N);
        BitSet B2 = new BitSet(N);
        for(int i = 0; i < M; ++i)
        {
            String operation = cin.next();
            int a = cin.nextInt(), b = cin.nextInt();

            if(operation.compareTo("AND") == 0)
            {
                if(a == 1) B1.and(B2); else B2.and(B1);
                System.out.println(B1.cardinality() + " " + B2.cardinality());
            }
            if(operation.compareTo("OR") == 0)
            {
                if(a == 1) B1.or(B2); else B2.or(B1);
                System.out.println(B1.cardinality() + " " + B2.cardinality());
            }
            if(operation.compareTo("XOR") == 0)
            {
                if(a == 1) B1.xor(B2); else B2.xor(B1);
                System.out.println(B1.cardinality() + " " + B2.cardinality());
            }
            if(operation.compareTo("FLIP") == 0)
            {
                if(a == 1) B1.flip(b); else B2.flip(b);
                System.out.println(B1.cardinality() + " " + B2.cardinality());
            }
            if(operation.compareTo("SET") == 0)
            {
                if(a == 1) B1.set(b); else B2.set(b);
                System.out.println(B1.cardinality() + " " + B2.cardinality());
            }
        }
    }
}

