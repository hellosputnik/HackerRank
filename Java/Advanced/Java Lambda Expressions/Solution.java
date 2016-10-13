public static PerformOperation is_odd()
{
    return (int i) -> { return (i % 2) != 0; };
}

public static PerformOperation is_prime()
{
    return (int i) -> { return java.math.BigInteger.valueOf(i).isProbablePrime(1337); };
}

public static PerformOperation is_palindrome()
{
    return (int i) -> {
        return i == Integer.parseInt(new StringBuilder(String.valueOf(i)).reverse().toString());
    };
}

