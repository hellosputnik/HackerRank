import math


def combination(n, r):
    return (math.factorial(n) / (math.factorial(n - r) * math.factorial(r)))


def binomial_distribution(x, n, p):
    q = (1 - p)
    return combination(n, x) * (p ** x) * (q ** (n - x))


def main():
    odds = 0.12

    print round(sum([binomial_distribution(b, 10, odds) for b in xrange(0, 3)]), 3)
    print round(sum([binomial_distribution(b, 10, odds) for b in xrange(2, 11)]), 3)

if __name__ == '__main__':
    main()

