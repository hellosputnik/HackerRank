import java.io.*;
import java.math.*;
import java.util.*;

public class Solution
{
    public static void main(String [] args)
    {
        Scanner cin = new Scanner(System.in);

        BigInteger a = new BigInteger(cin.nextLine());
        BigInteger b = new BigInteger(cin.nextLine());

        System.out.printf("%d\n%d\n", a.add(b), a.multiply(b));
    }
}

