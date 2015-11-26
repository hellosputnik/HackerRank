import java.io.*;
import java.util.*;

public class Solution
{
    public static void main(String [] args)
    {
        Scanner cin = new Scanner(System.in);

        int t = Integer.parseInt(cin.nextLine());
        for(int T = 0; T < t; ++T)
        {
            String [] numbers = cin.nextLine().split(" ");

            int a = Integer.parseInt(numbers[0]);
            int b = Integer.parseInt(numbers[1]);
            int n = Integer.parseInt(numbers[2]);

            for(int N = 0; N < n; ++N)
            {
                a += Math.pow(2, N) * b;
                System.out.printf("%d ", a);
            }
            System.out.println();
        }
    }
}

