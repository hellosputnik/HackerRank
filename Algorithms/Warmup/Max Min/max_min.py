def unfair(N, K):

    minimum = max(N)

    for n in xrange(len(N) - K):
        unfairness = N[(n + K - 1)] - N[n]
        minimum = unfairness if unfairness < minimum else minimum

    return minimum

def main():

    N = input()
    K = input()

    integers = []
    for n in xrange(N):
        integers.append(input())

    print unfair(sorted(integers), K) 

if __name__ == '__main__':
    main()
