// This is necessary for System.in
import static java.lang.System.*;

class Prime
{
    public void checkPrime(int... numbers)
    {
        for(int n = 0; n < numbers.length; ++n)
        {
            if(BigInteger.valueOf(numbers[n]).isProbablePrime(1337))
                System.out.print(numbers[n] + " ");
        }
        System.out.print("\n");
    }
}
