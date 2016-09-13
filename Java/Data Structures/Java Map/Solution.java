import java.io.*;
import java.util.*;

public class Solution
{
    public static void main(String [] args)
    {
        Scanner cin = new Scanner(System.in);

        int n = cin.nextInt();
        cin.nextLine();

        Map<String, String> contacts = new HashMap();
        for(int i = 0; i < n; ++i)
        {
            String name = cin.nextLine(), number = cin.nextLine();
            contacts.put(name, number);
        }

        String query;
        while(cin.hasNextLine())
        {
            query = cin.nextLine();
            String number = contacts.get(query);
            if(number != null)
                System.out.println(query + "=" + number);
            else
                System.out.println("Not found");
        }
    }
}
