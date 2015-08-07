def main():
    N = input()

    matrix = []
    for n in xrange(N):
        matrix.extend([map(int, raw_input().split())])

    first, second = 0, 0
    for n in xrange(N):
        first += matrix[n][n]
        second += matrix[n][(-n - 1)]

    print abs(first - second)

if __name__ == '__main__':
    main()

