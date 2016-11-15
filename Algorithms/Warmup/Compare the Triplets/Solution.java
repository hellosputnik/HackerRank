import java.util.*;

public class Solution
{
    public static void main(String [] args)
    {
        Scanner cin = new Scanner(System.in);

        int a0, a1, a2;
        int b0, b1, b2;

        a0 = cin.nextInt();
        a1 = cin.nextInt();
        a2 = cin.nextInt();

        b0 = cin.nextInt();
        b1 = cin.nextInt();
        b2 = cin.nextInt();

        int A = 0, B = 0;

        A += (a0 > b0) ? 1 : 0;
        B += (a0 < b0) ? 1 : 0;

        A += (a1 > b1) ? 1 : 0;
        B += (a1 < b1) ? 1 : 0;

        A += (a2 > b2) ? 1 : 0;
        B += (a2 < b2) ? 1 : 0;

        System.out.println(A + " " + B);
    }
}

