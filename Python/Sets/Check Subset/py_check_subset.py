for t in xrange(input()):
    a, A = input(), set(map(int, raw_input().split()))
    b, B = input(), set(map(int, raw_input().split()))

    print A.issubset(B)

