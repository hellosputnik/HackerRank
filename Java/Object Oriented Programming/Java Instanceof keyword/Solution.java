import java.util.*;

class Hacker {}
class Rockstar {}
class Student {}

public class InstanceOfTutorial
{
    private static String count(ArrayList myList)
    {
        int a = 0, b = 0, c = 0;

        for(int i = 0; i < myList.size(); ++i)
        {
            Object element = myList.get(i);
            if(element instanceof Student)
                ++a;
            if(element instanceof Rockstar)
                ++b;
            if(element instanceof Hacker)
                ++c;
        }

        return Integer.toString(a) + " " + Integer.toString(b) + " " + Integer.toString(c);
    }

    public static void main(String [] args)
    {
        ArrayList myList = new ArrayList();
        Scanner cin = new Scanner(System.in);

        int t = cin.nextInt();

        for(int i = 0; i < t; ++i)
        {
            String s = cin.next();
            if(s.equals("Student"))
                myList.add(new Student());
            if(s.equals("Rockstar"))
                myList.add(new Rockstar());
            if(s.equals("Hacker"))
                myList.add(new Hacker());
        }

        System.out.println(count(myList));
    }
}
