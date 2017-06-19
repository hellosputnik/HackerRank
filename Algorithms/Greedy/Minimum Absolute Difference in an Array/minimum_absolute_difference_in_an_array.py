def main():
    n = input()
    a = map(int, raw_input().split())

    a.sort()

    minimum = a[-1] - a[0]

    for index, element in enumerate(a):
        difference = abs(element - a[index - 1])
        minimum    = min(minimum, difference)

    print minimum


if __name__ == '__main__':
    main()

