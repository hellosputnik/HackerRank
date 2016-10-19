import numpy

def main():
    N, M, P = map(int, raw_input().split())

    lines = []
    for n in xrange(N):
        line = map(int, raw_input().split())
        lines.append(line)

    arrayN = numpy.array(lines)

    lines = []
    for m in xrange(M):
        line = map(int, raw_input().split())
        lines.append(line)

    arrayM = numpy.array(lines)

    print numpy.concatenate((arrayN, arrayM), axis=0)


if __name__ == '__main__':
    main()

