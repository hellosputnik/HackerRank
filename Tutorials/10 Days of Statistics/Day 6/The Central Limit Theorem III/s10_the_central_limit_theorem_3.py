import math


def main():
    sample_size        = input()
    mean               = input()
    standard_deviation = input()
    coverage           = input()
    z_score            = input()

    sample_standard_deviation = standard_deviation / math.sqrt(sample_size)

    print round(mean - z_score * sample_standard_deviation, 2)
    print round(mean + z_score * sample_standard_deviation, 2)


if __name__ == '__main__':
    main()

