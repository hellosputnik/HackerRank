import java.security.*;
import java.util.*;

public class Solution
{
    public static void main(String [] args) throws Exception
    {
        Scanner cin = new Scanner(System.in);
        MessageDigest md = MessageDigest.getInstance("MD5");


        String message = cin.next();
        md.update(message.getBytes());

        byte [] bytes = md.digest();
        for(int i = 0; i < bytes.length; ++i)
            System.out.print(String.format("%02x", bytes[i]));
    }
}
