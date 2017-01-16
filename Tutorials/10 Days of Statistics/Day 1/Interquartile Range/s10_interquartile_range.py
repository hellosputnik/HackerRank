import itertools


def median(array):
    array, length = sorted(array), len(array)

    if length % 2 != 0:
        return array[(length / 2)]
    else:
        left, right = array[((length / 2) - 1)], array[(length / 2)]
        return ((left + right) / float(2))


def main():
    n = input()
    X = map(int, raw_input().split())
    F = map(int, raw_input().split())

    array = [list(itertools.repeat(X[i], f)) for i, f in enumerate(F)]
    array = sorted(list(itertools.chain(*array)))

    # Lower quartile
    lower = median(array[:(len(array) / 2)])

    # Upper quartile
    if len(array) % 2 == 0:
        upper = median(array[(len(array) / 2):])
    else:
        upper = median(array[((len(array) / 2) + 1):])

    print float(upper - lower)


if __name__ == '__main__':
    main()

