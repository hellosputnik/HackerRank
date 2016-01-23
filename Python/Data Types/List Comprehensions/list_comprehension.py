def main():
    X, Y, Z, N = (input() for _ in xrange(4))

    print [[x, y, z] for x in xrange(X + 1) for y in xrange(Y + 1) for z in xrange(Z + 1) if sum([x, y, z]) != N]

if __name__ == '__main__':
    main()

