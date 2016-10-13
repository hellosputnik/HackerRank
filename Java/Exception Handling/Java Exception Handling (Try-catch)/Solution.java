import java.io.*;
import java.lang.*;
import java.util.*;

public class Solution
{
    public static void main(String [] args) throws IOException
    {
        Scanner cin = new Scanner(System.in);

        try
        {
            int x = cin.nextInt();
            int y = cin.nextInt();

            int quotient = x / y;

            System.out.println(quotient);
        }
        catch (ArithmeticException e)
        {
            System.out.println(e);
        }
        catch (InputMismatchException e)
        {
            System.out.println(e.getClass().getName());
        }
    }
}
