def check(G, P):
    R, C, r, c = len(G), len(G[0]), len(P), len(P[0])
    X, Y = (C - c), (R - r)

    for y in xrange(Y + 1):
        for x in xrange(X + 1):
            if G[y][x:(x + c)] == P[0]:
                flag = True
                for i in xrange(1, r):
                    if G[(y + i)][x:(x + c)] != P[i]:
                        flag = False
                if flag:
                    return "YES"
    
    return "NO"

def main():
    T = input()

    for t in xrange(T):

        G = []
        R, C = map(int, raw_input().split())
        for row in xrange(R):
            G.append([int(number) for number in raw_input()])

        P = []
        r, c = map(int, raw_input().split())
        for row in xrange(r):
            P.append([int(number) for number in raw_input()])

        print check(G, P)

if __name__ == '__main__':
    main()

