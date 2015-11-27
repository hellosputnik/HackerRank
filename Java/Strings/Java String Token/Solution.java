import java.io.*;
import java.util.*;

public class Solution
{
    public static void main(String [] args)
    {
        Scanner cin = new Scanner(System.in);

        String s = cin.nextLine().trim();
        if(s.length() == 0)
        {
            System.out.println(0);
            return;
        }

        String [] tokens = s.split("[ !,?.\\_'@]+");

        System.out.println(tokens.length);
        for(String t : tokens)
            System.out.println(t);
    }
}

