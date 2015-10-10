import java.io.*;
import java.util.*;

// Change the class name to solution to submit on HackerRank
public class prng_sequence_guessing
{
    public static void main(String [] args) 
    {
        int N;

        Scanner cin = new Scanner(System.in);
        N = cin.nextInt();

        for(int n = 0; n < N; ++n)
        {
            long start, end;
            int[] output = new int[20];

            // Get start time, end time, and 10 PRNG numbers
            start = cin.nextLong();
            end = cin.nextLong();
            for(int i = 0; i < 10; ++i)
                output[i] = cin.nextInt();

            // Search for seed
            for(long seed = start; seed < end; ++seed)
            {
                int number;
                Random random = new Random(seed);
                boolean found = true;

                // Get initial 10 PRNG numbers
                for(int i = 0; i < 10; ++i)
                {
                    number = random.nextInt(1000);
                    if(number != output[i])
                    {
                        found = false;
                        break;
                    }
                }

                // Get subsequent 10 PRNG numbers if initial numbers matched
                if(found)
                {
                    System.out.print(seed + " ");
                    for(int i = 0; i < 10; ++i)
                        System.out.print(random.nextInt(1000) + " ");
                    System.out.println();
                }
            }
        }
    }
}

