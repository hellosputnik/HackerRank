def function(x):
    for i in xrange(1, len(x)):
        if x[x[i]] != i:
            print "NO"
            return
    print "YES"


def main():
    n = input()
    y = [0]
    y.extend(map(int, raw_input().split()))

    function(y)

if __name__ == '__main__':
    main()

