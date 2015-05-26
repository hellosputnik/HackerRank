def funny(S):
    R = S[::-1]

    S, R = map(ord, S), map(ord, R)

    for i in xrange(1, len(S)):
        if abs(S[i] - S[(i - 1)]) != abs(R[i] - R[(i - 1)]):
            return "Not Funny"

    return "Funny"

def main():
    T = input()

    for t in xrange(T):
        S = raw_input()
        print funny(S)

if __name__ == '__main__':
    main()

