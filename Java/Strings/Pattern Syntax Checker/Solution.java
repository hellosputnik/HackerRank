import java.io.*;
import java.util.*;
import java.util.regex.*;

public class Solution
{
    public static void main(String [] args)
    {
        Scanner cin = new Scanner(System.in);

        int N = Integer.parseInt(cin.nextLine());
        for(int n = 0; n < N; ++n)
        {
            String pattern = cin.nextLine();
            try
            {
                Pattern.compile(pattern);
                System.out.println("Valid");
            }
            catch(Exception e)
            {
                System.out.println("Invalid");
            }
        }
    }
}

