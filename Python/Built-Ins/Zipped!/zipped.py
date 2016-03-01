def main():
    N, X = map(int, raw_input().split())

    scores = []
    for x in xrange(X):
        scores.append(map(float, raw_input().split()))

    for score in zip(*scores):
        print (sum(score) / len(score))

if __name__ == '__main__':
    main()

