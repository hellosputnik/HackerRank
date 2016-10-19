import numpy

def main():
    N, M = map(int, raw_input().split())

    lines = []
    for n in xrange(N):
        line = map(int, raw_input().split())
        lines.append(line)

    array = numpy.array(lines)
    print numpy.prod(numpy.sum(array, axis=0))


if __name__ == '__main__':
    main()

