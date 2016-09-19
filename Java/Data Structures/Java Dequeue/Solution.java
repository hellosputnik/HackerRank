import java.io.*;
import java.util.*;

public class Solution
{
    public static void main(String [] args)
    {
        Scanner cin = new Scanner(System.in);
        int N = cin.nextInt(), M = cin.nextInt();
        Deque<Integer> deque = new LinkedList();
        Map<Integer, Integer> map = new HashMap();

        int max = 0;
        for(int n = 0; n < N; ++n)
        {
            int x = cin.nextInt();
            deque.add(x);
            Integer y = map.get(x);
            if(y != null)
                map.put(x, y + 1);
            else
                map.put(x, 1);

            if(deque.size() == M)
            {
                int size = map.keySet().size();
                if(size > max)
                    max = size;

                int key = deque.remove();
                Integer value = map.get(key);
                if(value != null)
                {
                    if(value == 1)
                        map.remove(key);
                    else
                        map.put(key, value - 1);
                }
            }
        }

        System.out.println(max);
    }
}

