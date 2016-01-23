def main():
    A = set(raw_input().split())
    N = input()

    result = True
    for n in xrange(N):
        result &= (A > set(raw_input().split()))

    print result


if __name__ == '__main__':
    main()

