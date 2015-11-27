import java.io.*;
import java.util.*;

public class Solution
{
    public static void main(String [] args)
    {
        Scanner cin = new Scanner(System.in);

        String A = cin.next();
        String B = cin.next();

        System.out.printf("%d\n", A.length() + B.length());

        if(A.compareTo(B) > 0)
            System.out.printf("Yes\n");
        else
            System.out.printf("No\n");

        A = Character.toUpperCase(A.charAt(0)) + A.substring(1);
        B = Character.toUpperCase(B.charAt(0)) + B.substring(1);

        System.out.printf("%s %s\n", A, B);
    }
}

