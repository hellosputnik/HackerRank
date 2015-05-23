def calculate(B, W, X, Y, Z):

    if X == Y:
        return ((B * X) + (W * Y))

    if X < Y:
        if (X + Z) < Y:
            return ((B * X) + (W * (X + Z)))
        else:
            return ((B * X) + (W * Y))
    else:
        if (Y + Z) < X:
            return ((B * (Y + Z)) + (W * Y))
        else:
            return ((B * X) + (W * Y))

def main():
    T = input()

    for t in xrange(T):
        B, W = map(int, raw_input().split())
        X, Y, Z = map(int, raw_input().split())
        
        print calculate(B, W, X, Y, Z)

if __name__ == '__main__':
    main()
