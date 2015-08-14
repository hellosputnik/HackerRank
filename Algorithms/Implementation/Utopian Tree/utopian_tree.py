T = input()

# O(n)
def f(N):
    x = 1

    for n in xrange(N):
        if n % 2:
            x += 1
        else:
            x *= 2

    return x

# O(1)
def s(N):
    if N == 0:
        return 1
    else:
        return (4 << ((N - 1) / 2)) - 1 - (N & 1)

for t in xrange(T):
    N = input()
    print s(N)

