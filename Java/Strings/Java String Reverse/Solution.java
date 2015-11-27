import java.io.*;
import java.util.*;

public class Solution
{
    public static void main(String [] args)
    {
        Scanner cin = new Scanner(System.in);

        String A = cin.nextLine();

        if(A.compareTo(new StringBuilder(A).reverse().toString()) == 0)
            System.out.printf("Yes\n");
        else
            System.out.printf("No\n");
    }
}

