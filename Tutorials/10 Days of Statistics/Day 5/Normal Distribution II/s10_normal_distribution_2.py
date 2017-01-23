import math


def normalize(x, mean, std_dev):
    return 0.5 * (1 + math.erf((x - mean) / (std_dev * math.sqrt(2))))


def main():
    mean, std_dev = map(float, raw_input().split())

    a = input()
    b = input()

    print round((1 - normalize(a, mean, std_dev)) * 100, 2)
    print round((1 - normalize(b, mean, std_dev)) * 100, 2)
    print round(normalize(b, mean, std_dev) * 100, 2)


if __name__ == '__main__':
    main()

