import java.io.*;
import java.util.*;

public class Solution
{
    public static void main(String [] args)
    {
        Scanner cin = new Scanner(System.in);

        String s = cin.nextLine();
        int k = cin.nextInt();

        String max = s.substring(0, k), min = s.substring(0, k);
        for(int n = 0; n <= (s.length() - k); ++n)
        {
            String buffer = s.substring(n, (n + k));

            if(buffer.compareTo(max) > 0)
                max = buffer;
            if(buffer.compareTo(min) < 0)
                min = buffer;
        }

        System.out.printf("%s\n%s\n", min, max);
    }
}

