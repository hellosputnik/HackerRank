def main():
    n, m = map(int, raw_input().split())
    A = map(int, raw_input().split())
    B = map(int, raw_input().split())

    results = []
    for i in xrange(min(A), max(B) + 1):
        if all([i % a == 0 for a in A]) and all([b % i == 0 for b in B]):
            results.append(i)
    print len(results)


if __name__ == '__main__':
    main()

