def main():
    N = input()

    width = len("{0:b}".format(N))
    for n in xrange(N):
        print "{0:{w}d} {0:{w}o} {0:{w}X} {0:{w}b}".format((n + 1), w = width)

if __name__ == '__main__':
    main()

