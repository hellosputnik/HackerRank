import java.io.*;
import java.util.*;

public class Solution
{
    public static void main(String [] args)
    {
        Scanner cin = new Scanner(System.in);

        int n = cin.nextInt();

        PriorityQueue<Student> queue = new PriorityQueue(n, new Checker());
        for(int i = 0; i < n; ++i)
        {
            String event = cin.next();

            if(event.compareTo("ENTER") == 0)
            {
                String name = cin.next();
                double CGPA = cin.nextDouble();
                int token = cin.nextInt();

                queue.add(new Student(name, CGPA, token));
            } else {
                queue.poll();
            }
        }

        if(queue.isEmpty())
        {
            System.out.println("EMPTY");
        } else {
            while(!queue.isEmpty())
                System.out.println(queue.poll().name);
        }
    }
}

class Student
{
    public String name;
    public int CGPA;
    public int token;

    public Student(String name, double CGPA, int token)
    {
        this.name = name;
        this.CGPA = (int)(CGPA * 100);
        this.token = token;
    }
}

class Checker implements Comparator<Student>
{
    public int compare(Student s1, Student s2)
    {
        if(s2.CGPA == s1.CGPA)
        {
            if(s1.name.compareTo(s2.name) == 0)
                return s1.token - s2.token;

            return s1.name.compareTo(s2.name);
        }

        return s2.CGPA - s1.CGPA;
    }
}

