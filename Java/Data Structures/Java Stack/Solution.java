import java.io.*;
import java.util.*;

public class Solution
{
    public static void main(String [] args)
    {
        Scanner cin = new Scanner(System.in);

        while(cin.hasNext())
        {
            String line = cin.nextLine();
            System.out.println(check(line));
        }
    }

    private static boolean check(String str)
    {
        Stack<Character> stack = new Stack();

        for(int i = 0; i < str.length(); ++i)
        {
            char c = str.charAt(i);

            if("({[".indexOf(c) >= 0)
            {
                stack.push(c);
            } else {
                if(stack.empty())
                    return false;

                switch(c)
                {
                case ')':
                    if('(' != stack.pop())
                        return false;
                    break;
                case '}':
                    if('{' != stack.pop())
                        return false;
                    break;
                case ']':
                    if('[' != stack.pop())
                        return false;
                    break;
                default:
                    System.out.println("Something went horribly wrong!");
                }
            }
        }
        return stack.empty() ? true : false;
    }
}

