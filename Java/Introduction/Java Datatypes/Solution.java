import java.util.*;

public class Solution
{
    public static void main(String [] args)
    {
        Scanner cin = new Scanner(System.in);

        int T = Integer.parseInt(cin.nextLine());

        for(int t = 0; t < T; ++t)
        {
            String number = cin.nextLine();

            try
            {
                long l = Long.parseLong(number);

                System.out.println(number + " can be fitted in:");

                if(l >= -128 && l <= 127)
                    System.out.println("* byte");

                if(l >= -32768 && l <= 32767)
                    System.out.println("* short");

                if(l >= -2147483648 && l <= 2147483647)
                    System.out.println("* int");

                if(l >= -9223372036854775808l && l <= 9223372036854775807l)
                    System.out.println("* long");
            }
            catch(Exception e)
            {
                System.out.println(number + " can't be fitted anywhere.");
            }
        }
    }
}

