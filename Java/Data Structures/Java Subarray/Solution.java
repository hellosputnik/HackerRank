import java.io.*;
import java.util.*;

public class Solution
{
    public static void main(String [] args)
    {
        Scanner cin = new Scanner(System.in);
        int n = cin.nextInt();
        int A [] = new int[n];

        int count = 0;
        for(int i = 0; i < n; ++i)
        {
            A[i]= cin.nextInt();
            int a = A[i];

            if(a < 0)
                ++count;
            for(int offset = 1; offset <= i; ++offset)
            {
                a += A[i - offset];
                if(a < 0)
                    ++count;
            }
        }

        System.out.println(count);
    }
}

