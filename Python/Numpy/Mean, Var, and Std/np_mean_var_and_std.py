import numpy

def main():
    N, M = map(int, raw_input().split())

    lines = []
    for n in xrange(N):
        line = map(int, raw_input().split())
        lines.append(line)

    array = numpy.array(lines)

    print numpy.mean(array, axis=1)
    print numpy.var(array, axis=0)
    print numpy.std(array, axis=None)


if __name__ == '__main__':
    main()

