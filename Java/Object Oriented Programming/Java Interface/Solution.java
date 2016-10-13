class MyCalculator implements AdvancedArithmetic
{
    public int divisor_sum(int n)
    {
        int sum = 0;

        // Note: This is a terribly inefficient algorithm. For optimization,
        //       the loop add factors in pairs and end at sqrt(n).
        for(int i = 1; i <= n; ++i)
            if(n % i == 0)
                sum += i;

        return sum;
    }
}
