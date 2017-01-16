import math


def mean(array):
    return (sum(array) / len(array))


def stdev(array):
    average = mean(array)

    total = 0
    for x in array:
        total += ((x - average) ** 2)
    return math.sqrt(total / len(array))


def main():
    N = input()
    X = map(int, raw_input().split())

    print stdev(X)


if __name__ == '__main__':
    main()

