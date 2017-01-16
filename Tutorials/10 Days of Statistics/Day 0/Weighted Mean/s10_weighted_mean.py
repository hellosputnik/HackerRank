def mean(array, weights):
    total = 0
    for index, value in enumerate(array):
        total += value * weights[index]
    return (float(total) / sum(weights))


def main():
    N = input()
    X = map(int, raw_input().split())
    W = map(int, raw_input().split())

    print round(mean(X, W), 1)


if __name__ == '__main__':
    main()

