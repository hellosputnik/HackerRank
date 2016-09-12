import java.io.*;
import java.util.*;

public class Solution
{
    public static void main(String [] args)
    {
        Scanner cin = new Scanner(System.in);

        int T = cin.nextInt();
        for(int t = 0; t < T; ++t)
        {
            int n = cin.nextInt();
            int m = cin.nextInt();

            int array[] = new int[n];
            boolean visited[] = new boolean[n];
            for(int i = 0; i < n; ++i)
            {
                array[i] = cin.nextInt();
                visited[i] = false;
            }

            System.out.println(play(m, array, 0, visited) ? "YES" : "NO");
        }
    }

    private static boolean play(int jump, int array[], int index, boolean visited[])
    {
        if(index < 0 || visited[index] || array[index] == 1)
            return false;
        visited[index] = true;
        if(index + 1 >= array.length || index + jump >= array.length)
            return true;
        return play(jump, array, index + 1, visited) ||
               play(jump, array, index - 1, visited) ||
               play(jump, array, index + jump, visited);
    }
}

