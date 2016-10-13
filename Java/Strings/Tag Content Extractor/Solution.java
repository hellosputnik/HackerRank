import java.util.*;
import java.util.regex.*;

public class Solution
{
    public static void main(String [] args)
    {
        Scanner cin = new Scanner(System.in);

        int N = cin.nextInt();

        // Consume newline left by nextInt()
        cin.nextLine();

        for(int i = 0; i < N; ++i)
        {
            String line = cin.nextLine();
            parse(line);
        }
    }

    private static void parse(String string)
    {
        int matches = 0;

        Pattern p = Pattern.compile("<(.+?)>([^<>]+)</\\1>");
        Matcher m = p.matcher(string);

        while(m.find())
        {
            if(m.group(2).length() > 0)
            {
                System.out.println(m.group(2));
                ++matches;
            }
        }

        if(matches == 0)
            System.out.println("None");
    }
}
