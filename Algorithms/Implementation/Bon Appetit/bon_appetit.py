def main():
    n, k = map(int, raw_input().split())
    c = map(int, raw_input().split())
    b = input()

    difference = (((sum(c) - c[k]) / 2) - b)
    print "Bon Appetit" if difference == 0 else abs(difference)


if __name__ == '__main__':
    main()

