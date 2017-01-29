def distribute(loaves, persons):
    count = 0

    for i in xrange(persons - 2):
        if loaves[i] % 2:
            if i != 0 and loaves[(i - 1)] % 2:
                loaves[(i - 1)] += 1
                loaves[i] += 1
            else:
                loaves[i] += 1
                loaves[(i + 1)] += 1
            count += 2

    if loaves[(persons - 1)] % 2 and loaves[(persons - 2)]:
        loaves[(persons - 1)] += 1
        loaves[(persons - 2)] += 1
        count += 2

    return count if all(map(lambda x: x % 2 == 0, loaves)) else "NO"


def main():
    N = input()
    loaves = map(int, raw_input().split())

    print distribute(loaves, N)


if __name__ == '__main__':
    main()

