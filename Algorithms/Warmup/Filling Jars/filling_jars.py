N, M = map(int, raw_input().split())

total = 0
for m in xrange(M):
    a, b, k = map(int, raw_input().split())
    total += ((b - a + 1) * k)

print total / N

