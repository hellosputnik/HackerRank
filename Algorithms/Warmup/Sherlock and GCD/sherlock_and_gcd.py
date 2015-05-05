import fractions
import itertools

def f(x):
    for combination in itertools.combinations(x, 2):
        if fractions.gcd(combination[0], combination[1]) == 1:
            return "YES"
    return "NO"
            

T = input()

for t in xrange(T):
    N = input()
    a = map(int, raw_input().split())
    print f(a)

