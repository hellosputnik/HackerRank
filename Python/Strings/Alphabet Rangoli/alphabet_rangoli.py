import collections

ALPHABET = "abcdefghijklmnopqrstuvwxyz"

def main():
    # Get size of rangoli
    N = input()

    # Calculate size of row
    size = ((4 * N) - 3)

    # First half of design (including center)
    for n in reversed(xrange(N)):
        base = collections.deque(ALPHABET[n])
        for offset in xrange(1, N - n):
            base.appendleft(ALPHABET[n + offset])
            base.append(ALPHABET[n + offset])
        print '-'.join(base).center(size, "-")

    # Second half of design (excluding center)
    for n in xrange(1, N):
        base = collections.deque(ALPHABET[n])
        for offset in xrange(1, N - n):
            base.appendleft(ALPHABET[n + offset])
            base.append(ALPHABET[n + offset])
        print '-'.join(base).center(size, "-")

if __name__ == '__main__':
    main()

