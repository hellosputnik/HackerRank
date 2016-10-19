import collections

def main():
    S, K = raw_input(), input()

    N = len(S)

    for i in xrange(0, N, K):
        print "".join(collections.OrderedDict.fromkeys(S[i:(i+K)]))

if __name__ == '__main__':
    main()

