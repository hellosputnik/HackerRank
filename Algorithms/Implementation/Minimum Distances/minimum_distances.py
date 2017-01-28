def minimum(array):
    seen = {}

    minimum = len(array)
    for index, element in enumerate(array):
        if element in seen:
            minimum = min((index - seen[element]), minimum)
            seen[element] = index
        else:
            seen[element] = index

    return -1 if minimum == len(array) else minimum


def main():
    n = input()
    A = map(int, raw_input().split())

    print minimum(A)


if __name__ == '__main__':
    main()

