N, T = map(int, raw_input().split())
width = map(int, raw_input().split())

for t in xrange(T):
    i, j = map(int, raw_input().split())
    print min(width[i:(j + 1)])

