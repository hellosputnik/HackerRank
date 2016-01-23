N, M = map(int, raw_input().split())

for n in xrange(1, N - 1, 2):
    print ''.join(['.|.'] * n).center(M, '-')
    
print "WELCOME".center(M, "-")

for n in reversed(xrange(1, N - 1, 2)):
    print ''.join(['.|.'] * n).center(M, '-')

