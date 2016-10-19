import numpy

def main():
    N = map(int, raw_input().split())

    print numpy.zeros(N, dtype=numpy.int)
    print numpy.ones(N, dtype=numpy.int)


if __name__ == '__main__':
    main()

