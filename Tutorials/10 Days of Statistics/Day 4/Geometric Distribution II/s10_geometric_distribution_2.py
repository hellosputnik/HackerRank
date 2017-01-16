def geometric_distribution(n, p):
    q = 1 - p
    return (q ** (n - 1) * p)


def main():
    # n is for numerator; d is for denominator.
    n, d = map(int, raw_input().split())
    # i is the number of inspections/trials.
    i = input()

    p = [geometric_distribution(trial, float(n) / d) for trial in xrange(1, i + 1)]
    print round(sum(p), 3)


if __name__ == '__main__':
    main()

