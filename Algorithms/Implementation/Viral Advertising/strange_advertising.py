import math


def f(x):
    while True:
        result = math.floor(x / 2)
        yield result
        x = result * 3


def main():
    n = input()

    count = 0
    generate = f(5)
    for day in xrange(n):
        count += next(generate)
    print int(count)


if __name__ == '__main__':
    main()

