def main():
    s, t = map(int, raw_input().split())
    a, b = map(int, raw_input().split())
    m, n = map(int, raw_input().split())
    apples = map(int, raw_input().split())
    oranges = map(int, raw_input().split())

    print len(filter(lambda x: (a + x) >= s and (a + x) <= t, apples))
    print len(filter(lambda x: (b + x) >= s and (b + x) <= t, oranges))


if __name__ == '__main__':
    main()

