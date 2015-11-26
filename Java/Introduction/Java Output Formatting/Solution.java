import java.io.*;
import java.util.*;

public class Solution
{
    public static void main(String [] args)
    {
        Scanner cin = new Scanner(System.in);

        System.out.println("================================"); 
        for(int n = 0; n < 3; ++n)
        {
            String s = cin.next();
            int i = cin.nextInt();

            System.out.printf("%-15s%03d\n", s, i);
        }
        System.out.println("================================"); 
    }
}

