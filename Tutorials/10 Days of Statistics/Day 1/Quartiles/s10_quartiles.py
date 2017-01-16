def median(array):
    array, length = sorted(array), len(array)

    if length % 2 != 0:
        return array[(length / 2)]
    else:
        left, right = array[((length / 2) - 1)], array[(length / 2)]
        return ((left + right) / 2)


def main():
    n = input()
    X = map(int, raw_input().split())

    array = sorted(X)

    # Lower quartile
    print median(array[:(len(array) / 2)])

    # Median
    print median(array)

    # Upper quartile
    if len(array) % 2 == 0:
        print median(array[(len(array) / 2):])
    else:
        print median(array[((len(array) / 2) + 1):])


if __name__ == '__main__':
    main()

