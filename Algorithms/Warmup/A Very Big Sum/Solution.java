import java.math.*;
import java.util.*;

public class Solution
{
    public static void main(String [] args)
    {
        Scanner cin = new Scanner(System.in);
        int N = cin.nextInt();

        BigInteger sum = BigInteger.valueOf(0);
        for(int n = 0; n < N; ++n)
        {
            sum = sum.add(BigInteger.valueOf(cin.nextInt()));
        }

        System.out.println(sum);
    }
}
