import java.io.*;
import java.util.*;

public class Solution
{
    public static void main(String [] args)
    {
        Scanner cin = new Scanner(System.in);

        int n = cin.nextInt();
        ArrayList<int[]> numbers = new ArrayList();

        for(int i = 0; i < n; ++i)
        {
            int d = cin.nextInt();
            int array [] = new int[d];

            for(int x = 0; x < d; ++x)
                array[x] = cin.nextInt();

            numbers.add(array);
        }

        int q = cin.nextInt();
        for(int i = 0; i < q; ++i)
        {
            int x = cin.nextInt() - 1, y = cin.nextInt() - 1;

            if(y < numbers.get(x).length)
                System.out.println(numbers.get(x)[y]);
            else
                System.out.println("ERROR!");
        }
    }
}
