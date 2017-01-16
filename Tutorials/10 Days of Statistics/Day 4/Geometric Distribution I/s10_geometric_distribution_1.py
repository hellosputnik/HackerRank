def geometric_distribution(n, p):
    q = 1 - p
    return (q ** (n - 1) * p)


def main():
    # n is for numerator; d is for denominator.
    n, d = map(int, raw_input().split())
    inspections = input()

    print round(geometric_distribution(inspections, float(n) / d), 3)


if __name__ == '__main__':
    main()

