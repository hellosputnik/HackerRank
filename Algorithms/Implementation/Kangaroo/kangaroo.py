def main():
    x1, v1, x2, v2 = map(int, raw_input().split())

    dx = x1 - x2
    dv = v2 - v1

    print "YES" if dv != 0 and dx / dv > 0 and dx % dv == 0 else "NO"


if __name__ == '__main__':
    main()

