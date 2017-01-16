import collections


def mean(array):
    total, length = sum(array), len(array)
    return (float(total) / length)


def median(array):
    array, length = sorted(array), len(array)

    # Check if there is an even amount of elements in the array
    if length % 2 != 0:
        return array[(length / 2)]
    else:
        left, right = array[((length / 2) -1)], array[(length / 2)]
        return ((float(left) + right) / 2)


def mode(array):
    counter = collections.Counter(array).most_common()
    return sorted(counter, key=lambda x: (-x[1], x[0]))[0][0]


def main():
    N = input()
    x = map(int, raw_input().split())

    print round(mean(x), 1)
    print round(median(x), 1)
    print mode(x)


if __name__ == '__main__':
    main()

