import numpy

def main():
    A = numpy.array(map(int, raw_input().split()))
    B = numpy.array(map(int, raw_input().split()))

    print numpy.inner(A, B)
    print numpy.outer(A, B)


if __name__ == '__main__':
    main()

