def f(N, K):
    if K == 0:
        return " ".join(map(str, range(1, N + 1)))

    if N % K == 0 and N / K % 2 == 0:
        permutation = []
        for i in xrange(N):
            if i / K % 2 == 0:
                permutation.append(i + 1 + K)
            else:
                permutation.append(i + 1 - K)
        return " ".join(map(str, permutation))
    else:
        return -1


def main():
    T = input()

    for t in xrange(T):
        N, K = map(int, raw_input().split())
        print f(N, K)


if __name__ == '__main__':
    main()

