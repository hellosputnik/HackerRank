import java.io.*;
import java.util.*;

public class Solution
{
    public static void main(String [] args)
    {
        Scanner cin = new Scanner(System.in);
        int array[][] = new int[6][6];

        for(int a = 0; a < 6; ++a)
            for(int b = 0; b < 6; ++b)
                array[a][b] = cin.nextInt();

        System.out.println(hourglass(array));
    }

    private static int hourglass(int array[][])
    {
        int max = -63, sum = 0;
        for(int row = 0; row < 4; ++row)
        {
            for(int column = 0; column < 4; ++column)
            {
                sum = 0;

                sum += array[row + 0][column + 0]; // UPPER LEFT
                sum += array[row + 0][column + 1]; // UPPER MID
                sum += array[row + 0][column + 2]; // UPPER RIGHT
                sum += array[row + 1][column + 1]; // MIDDLE
                sum += array[row + 2][column + 0]; // LOWER LEFT
                sum += array[row + 2][column + 1]; // LOWER MID
                sum += array[row + 2][column + 2]; // LOWER RIGHT

                if(sum > max)
                {
                    max = sum;
                    if(max == 63)
                        return max;
                }
            }
        }

        return max;
    }
}
