import java.io.*;
import java.util.*;

public class Solution
{
    /*
    private static boolean isAnagram(String A, String B)
    {
        char [] a = A.toLowerCase().toCharArray();
        char [] b = B.toLowerCase().toCharArray();

        Arrays.sort(a);
        Arrays.sort(b);

        if(new String(a).compareTo(new String(b)) == 0)
            return true;
        else
            return false;
    }
    */

    private static boolean isAnagram(String A, String B)
    {
        if(A.length() != B.length())
            return false;

        HashMap<Character, Integer> a = new HashMap<Character, Integer>();
        HashMap<Character, Integer> b = new HashMap<Character, Integer>();

        for(char c : A.toLowerCase().toCharArray())
            a.put(c, a.containsKey(c) ? (a.get(c) + 1) : 1);
        
        for(char c : B.toLowerCase().toCharArray())
            b.put(c, b.containsKey(c) ? (b.get(c) + 1) : 1);

        return a.equals(b);
    }

    public static void main(String [] args)
    {
        Scanner cin = new Scanner(System.in);

        String A = cin.next();
        String B = cin.next();

        if(isAnagram(A, B))
            System.out.printf("Anagrams");
        else
            System.out.printf("Not Anagrams");
    }
}

