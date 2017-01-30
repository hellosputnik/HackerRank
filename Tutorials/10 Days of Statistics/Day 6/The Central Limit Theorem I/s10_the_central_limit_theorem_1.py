import math


def normalize(x, mean, std_dev):
    return 0.5 * (1 + math.erf((x - mean) / (std_dev * math.sqrt(2))))


def main():
    maximum_weight     = input()
    number_of_boxes    = input()
    weight_of_box      = input()
    standard_deviation = input()

    u = number_of_boxes * weight_of_box
    o = math.sqrt(number_of_boxes) * standard_deviation

    print round(normalize(maximum_weight, u, o), 4)


if __name__ == '__main__':
    main()

