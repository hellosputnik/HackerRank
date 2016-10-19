import numpy

def main():
    N, M = map(int, raw_input().split())

    print numpy.eye(N, M)


if __name__ == '__main__':
    main()

