def f(x, y, z):
    answer = []

    for n in xrange(z):
        answer.append((x * (z - n - 1)) + (y * n))

    return " ".join(map(str, sorted(set(answer))))
        
T = input()

for t in xrange(T):
    n, a, b = input(), input(), input()
    print f(a, b, n)

