def main():
    N, Q = map(int, raw_input().split())

    seqList = [[] for n in xrange(N)]
    lastAns = 0

    for q in xrange(Q):
        type, x, y = map(int, raw_input().split())

        if type == 1:
            seqList[(x ^ lastAns) % N].append(y)
        if type == 2:
            seq = seqList[(x ^ lastAns) % N]
            lastAns = seq[y % len(seq)]
            print lastAns


if __name__ == '__main__':
    main()

