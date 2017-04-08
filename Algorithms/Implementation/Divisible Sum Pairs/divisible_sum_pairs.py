def main():
    n, k = map(int, raw_input().split())
    a = map(int, raw_input().split())

    count = 0
    for index, i in enumerate(a):
        for j in a[(index + 1):]:
            if (i + j) % k == 0:
                count += 1
    print count


if __name__ == '__main__':
    main()

