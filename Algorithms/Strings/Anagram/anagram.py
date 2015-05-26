def anagram(S):
    length = len(S)

    if length % 2:
        return -1

    S1, S2 = list(S[:(length / 2)]), list(S[(length / 2):])

    for s in S1:
        if s in S2:
            S2.remove(s)

    return len(S2)

def main():
    T = input()

    for t in xrange(T):
        S = raw_input()
        print anagram(S)

if __name__ == '__main__':
    main()

