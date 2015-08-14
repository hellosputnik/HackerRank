def main():
    d, m, y = map(int, raw_input().split())
    D, M, Y = map(int, raw_input().split())

    if y < Y:
        print 0
        return
    if y == Y and m < M:
        print 0
        return
    if y == Y and m == M and d <= D:
        print 0
        return

    if y > Y:
        print 10000
        return
    elif m > M:
        print (500 * (m - M))
        return
    else:
        print (15 * (d - D))
        return

if __name__ == '__main__':
    main()

