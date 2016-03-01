def main():
    N, M = map(int, raw_input().split())

    data = []
    for n in xrange(N):
        data.append(map(int, raw_input().split()))

    K = input()

    for row in sorted(data, key=lambda x: x[K]):
        print " ".join(map(str, row))

if __name__ == '__main__':
    main()

