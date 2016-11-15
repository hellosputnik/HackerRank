import java.util.*;

public class Solution
{
    public static void main(String [] args)
    {
        Scanner cin = new Scanner(System.in);
        int N = cin.nextInt();

        int sum = 0;
        for(int n = 0; n < N; ++n)
        {
            sum += cin.nextInt();
        }

        System.out.println(sum);
    }
}
