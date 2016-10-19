import numpy

def main():
    N, M = map(int, raw_input().split())

    lines = []
    for n in xrange(N):
        line = map(int, raw_input().split())
        lines.append(line)

    A = numpy.array(lines)

    lines = []
    for n in xrange(N):
        line = map(int, raw_input().split())
        lines.append(line)

    B = numpy.array(lines)

    print (A + B)
    print (A - B)
    print (A * B)
    print (A / B)
    print (A % B)
    print (A ** B)


if __name__ == '__main__':
    main()

