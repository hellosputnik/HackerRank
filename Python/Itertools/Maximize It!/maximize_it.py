import itertools

def main():
    K, M = map(int, raw_input().split())

    N = []
    for k in xrange(K):
        N.append(map(lambda x: int(x)**2, raw_input().split())[1:])

    products = list(itertools.product(*N))

    print reduce(max, map(lambda x: sum(x) % M, products))

if __name__ == '__main__':
    main()

