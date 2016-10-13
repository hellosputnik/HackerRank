import java.math.*;
import java.util.*;

public class Solution
{
    public static void main(String [] args)
    {
        Scanner cin = new Scanner(System.in);

        String n = cin.next();

        if(new BigInteger(n).isProbablePrime(1))
            System.out.println("prime");
        else
            System.out.println("not prime");
    }
}
