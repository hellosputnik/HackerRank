import java.io.*;
import java.util.*;

public class Solution
{
    public static void main(String [] args)
    {
        Scanner cin = new Scanner(System.in);

        for(int line = 1; cin.hasNext(); ++line)
            System.out.printf("%d %s\n", line, cin.nextLine());
    }
}

