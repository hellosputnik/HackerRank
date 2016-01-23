def main():
    n, m = map(int, raw_input().split())
    array = map(int, raw_input().split())
    A = set(map(int, raw_input().split()))
    B = set(map(int, raw_input().split()))

    happiness = 0

    for element in array:
        if element in A:
            happiness += 1
        if element in B:
            happiness -= 1

    print happiness

if __name__ == '__main__':
    main()
