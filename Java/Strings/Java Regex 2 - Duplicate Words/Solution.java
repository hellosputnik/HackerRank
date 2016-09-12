import java.util.*;
import java.util.regex.*;

public class Solution
{
    public static void main(String [] args)
    {

        String pattern = "(?i)\\b([a-z]+)\\b(?:\\s+\\1\\b)+";
        Pattern r = Pattern.compile(pattern);

        Scanner in = new Scanner(System.in);
        int testCases = Integer.parseInt(in.nextLine());
        while(testCases > 0)
        {
            String input = in.nextLine();
            Matcher m = r.matcher(input);
            boolean findMatch = true;
            while(m.find( ))
            {
                input = input.replaceAll(pattern, "$1");
                findMatch = false;
            }
            System.out.println(input);
            testCases--;
        }
    }
}

