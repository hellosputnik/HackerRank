T = input()

for t in xrange(T):
    A, B = map(int, raw_input().split())
    squares = int(B ** 0.5) - int(A ** 0.5)
    squares += 1 if int(A ** 0.5) ** 2 == A else 0
    print squares

