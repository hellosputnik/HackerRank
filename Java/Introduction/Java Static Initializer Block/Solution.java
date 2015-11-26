import java.io.*;
import java.util.*;

public class Solution
{
    public static boolean flag;
    public static int B;
    public static int H;

    static {
        Scanner cin = new Scanner(System.in);

        B = cin.nextInt();
        H = cin.nextInt();

        if(B > 0 && H > 0)
            flag = true;
        else
            System.out.println("java.lang.Exception: Breadth and height must be positive");
    }

    public static void main(String [] args)
    {
        if(flag) {
            int area = B * H;
            System.out.print(area);
        }
    }
}

