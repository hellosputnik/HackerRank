import numpy

def main():
    N = input()

    lines = []
    for n in xrange(N):
        line = map(float, raw_input().split())
        lines.append(line)

    array = numpy.array(lines)
    print numpy.linalg.det(array)


if __name__ == '__main__':
    main()

