import numpy

def main():
    numbers = map(int, raw_input().split())

    array = numpy.array(numbers)

    print numpy.reshape(array, (3, 3))


if __name__ == '__main__':
    main()

