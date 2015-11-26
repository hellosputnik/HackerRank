import java.io.*;
import java.util.*;

public class Solution
{
    public static void main(String [] args)
    {
        Scanner cin = new Scanner(System.in);

        int N = cin.nextInt();

        if(!(N % 2 == 0) || (N >= 6 && N <= 20))
            System.out.println("Weird");
        else
            System.out.println("Not Weird");
    }
}

