import math


def normalize(x, mean, std_dev):
    return 0.5 * (1 + math.erf((x - mean) / (std_dev * math.sqrt(2))))


def main():
    mean, std_dev = map(float, raw_input().split())

    a = input()
    b, c = map(float, raw_input().split())

    print round(normalize(a, mean, std_dev), 3)
    print round(normalize(c, mean, std_dev) - normalize(b, mean, std_dev), 3)


if __name__ == '__main__':
    main()

