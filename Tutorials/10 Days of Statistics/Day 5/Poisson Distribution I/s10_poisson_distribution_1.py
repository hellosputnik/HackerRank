mport math


def poisson_distribution(average, actual):
    e = 2.71828
    return ((average ** actual) * (e ** -(average)) / math.factorial(actual))


def main():
    mean = input()
    observed = input()

    print round(poisson_distribution(mean, observed), 3)


if __name__ == '__main__':
    main()

