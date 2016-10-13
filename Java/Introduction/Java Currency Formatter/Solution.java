import java.text.*;
import java.util.*;

public class Solution
{
    public static void main(String [] args)
    {
        Scanner cin = new Scanner(System.in);

        double payment = cin.nextDouble();

        String us     = NumberFormat.getCurrencyInstance().format(payment);
        String india  = NumberFormat.getCurrencyInstance(new Locale.Builder().setLanguage("en").setRegion("IN").build()).format(payment);
        String china  = NumberFormat.getCurrencyInstance(Locale.CHINA).format(payment);
        String france = NumberFormat.getCurrencyInstance(Locale.FRANCE).format(payment);

        System.out.println("US: "     + us);
        System.out.println("India: "  + india);
        System.out.println("China: "  + china);
        System.out.println("France: " + france);
    }
}
