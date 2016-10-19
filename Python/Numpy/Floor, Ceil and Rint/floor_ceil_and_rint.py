import numpy

def main():
    A = numpy.array(map(float, raw_input().split()))

    print numpy.floor(A)
    print numpy.ceil(A)
    print numpy.rint(A)


if __name__ == '__main__':
    main()

