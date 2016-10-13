import java.util.*;

public class Solution
{
    public static void main(String [] args)
    {
        Scanner cin = new Scanner(System.in);

        String s = cin.next();
        int start = cin.nextInt(), end = cin.nextInt();

        System.out.println(s.substring(start, end));
    }
}
