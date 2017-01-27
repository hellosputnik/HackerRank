def main():
    n = input()
    clouds = map(int, raw_input().split())

    i, steps = 0, 0
    while i != (n - 2) and i != (n - 1):
        if clouds[(i  + 2)]:
            i += 1
        else:
            i += 2
        steps += 1

    print (steps + 1)  if  i == (n - 2) else steps


if __name__ == '__main__':
    main()

