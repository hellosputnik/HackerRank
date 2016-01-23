def main():
    N = input()

    T = tuple(map(int, raw_input().split()))
    print hash(T)

if __name__ == '__main__':
    main()

