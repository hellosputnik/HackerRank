import itertools

def main():
    S, k = raw_input().split()

    S, k = sorted(S), int(k)
    for c in xrange(1, k + 1):
        for each in itertools.combinations(S, int(c)):
            print "".join(each)

if __name__ == '__main__':
    main()

