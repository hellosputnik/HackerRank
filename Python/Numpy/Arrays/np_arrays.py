import numpy

def main():
    numbers = raw_input().split()

    array = numpy.array(list(reversed(numbers)), float)

    print array

if __name__ == '__main__':
    main()

