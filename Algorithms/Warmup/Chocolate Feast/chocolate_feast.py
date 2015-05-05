T = input()

for t in xrange(T):
    N, C, M   = map(int, raw_input().split())
    print ((N / C) + ((N / C) - 1) / (M - 1))

