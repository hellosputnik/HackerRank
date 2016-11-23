def main():
    i, j, k = map(int, raw_input().split())

    count = 0
    for day in xrange(i, (j + 1)):
        if abs(day - int("".join(reversed(str(day))))) % k == 0:
            count += 1

    print count


if __name__ == '__main__':
    main()

