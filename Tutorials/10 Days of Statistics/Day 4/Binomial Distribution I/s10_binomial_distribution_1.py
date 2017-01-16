import math


def combination(n, r):
    return (math.factorial(n) / (math.factorial(n - r) * math.factorial(r)))


def binomial_distribution(x, n, p):
    q = (1 - p)
    return combination(n, x) * (p ** x) * (q ** (n - x))


def main():
    B, G = map(float, raw_input().split())
    odds = B / (B + G)

    # Calculate the probability for 3, 4, 5, and 6 boys.
    print round(sum([binomial_distribution(b, 6, odds) for b in xrange(3, 7)]), 3)


if __name__ == '__main__':
    main()

