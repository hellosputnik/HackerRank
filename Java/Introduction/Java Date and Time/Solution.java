import java.io.*;
import java.util.*;

public class Solution
{
    public static void main(String [] args)
    {
        Calendar calendar = Calendar.getInstance();
        Scanner cin = new Scanner(System.in);

        int month = Integer.parseInt(cin.next());
        int day = Integer.parseInt(cin.next());
        int year = Integer.parseInt(cin.next());

        // The months in Java are zero-based (i.e. Jan = 0, Feb = 1, etc.).
        calendar.set(year, (month - 1), day);
        int day_of_week = calendar.get(Calendar.DAY_OF_WEEK);

        // The weeks in Java are one-based and starts on Sunday.
        switch(day_of_week)
        {
        case 1:
            System.out.println("SUNDAY");
            break;
        case 2:
            System.out.println("MONDAY");
            break;
        case 3:
            System.out.println("TUESDAY");
            break;
        case 4:
            System.out.println("WEDNESDAY");
            break;
        case 5:
            System.out.println("THURSDAY");
            break;
        case 6:
            System.out.println("FRIDAY");
            break;
        case 7:
            System.out.println("SATURDAY");
            break;
        default:
            System.out.println("This line should never be reached.");
        }
    }
}
