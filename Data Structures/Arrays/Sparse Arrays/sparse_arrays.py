import collections


def main():
    N = input()

    strings = []
    for n in xrange(N):
        strings.append(raw_input())
        
    counter = collections.Counter(strings)

    Q = input()

    for q in xrange(Q):
        print counter[raw_input()]


if __name__ == '__main__':
    main()

