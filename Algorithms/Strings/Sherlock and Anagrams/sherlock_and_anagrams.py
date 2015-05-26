from collections import defaultdict
from math import factorial

def choose(n, r = 2):
    return (factorial(n) / (factorial(n - r) * factorial(r)))

def anagrams(S):
    length = len(S)

    substrings = defaultdict(list)
    for i in xrange(length):
        for j in xrange(i, length):
            substrings[((j + 1) - i)].append(''.join(sorted(S[i:(j + 1)])))

    pairs = 0
    for substring in substrings:
        uniques = set(substrings[substring])
        for unique in uniques:
            count = substrings[substring].count(unique)
            if count > 1:
                pairs += choose(count)

    return pairs

def main():
    T = input()

    for t in xrange(T):
        S = raw_input()
        print anagrams(S)

if __name__ == '__main__':
    main()

