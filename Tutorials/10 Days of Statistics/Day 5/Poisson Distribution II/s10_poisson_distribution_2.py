mport math


def poisson_distribution(average, actual):
    e = 2.71828
    return ((average ** actual) * (e ** -(average)) / math.factorial(actual))


def main():
    A, B = map(float, raw_input().split())

    print round(160 + 40 * (A + A * A), 3)
    print round(128 + 40 * (B + B * B), 3)


if __name__ == '__main__':
    main()

