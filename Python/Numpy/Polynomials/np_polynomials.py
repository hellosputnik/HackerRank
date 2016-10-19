import numpy

def main():
    coefficients = map(float, raw_input().split())
    x = input()

    print numpy.polyval(coefficients, x)


if __name__ == '__main__':
    main()

