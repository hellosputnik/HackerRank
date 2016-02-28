import collections

def main():
    n, m = map(int, raw_input().split())

    A = collections.defaultdict(list)
    for index in xrange(n):
        A[raw_input()].append(index + 1)

    for index in xrange(m):
        B = raw_input()
        if A[B]:
            print " ".join(map(str, A[B]))
        else:
            print -1

if __name__ == '__main__':
    main()

