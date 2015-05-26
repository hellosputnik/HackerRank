def main():
    N = input()

    for n in xrange(N):
        if n == 0:
            gemstones = set(raw_input())
        else:
            gemstones = gemstones.intersection(raw_input())

    print len(gemstones)

if __name__ == '__main__':
    main()

