import java.io.*;
import java.util.*;

public class Solution
{
    public static void main(String [] args)
    {
        Scanner cin = new Scanner(System.in);
        int N = cin.nextInt();

        List<Integer> L = new ArrayList<Integer>();

        for(int i = 0; i < N; ++i)
            L.add(cin.nextInt());

        int Q = cin.nextInt();
        for(int i = 0; i < Q; ++i)
        {
            cin.nextLine();
            String operation = cin.nextLine();

            if(operation.equals("Insert"))
            {
                int x = cin.nextInt(), y = cin.nextInt();
                L.add(x, y);
            } else {
                int x = cin.nextInt();
                L.remove(x);
            }
        }

        for(Integer i: L)
            System.out.print(i + " ");
    }
}

