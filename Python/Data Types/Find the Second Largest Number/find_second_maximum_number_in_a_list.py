def main():
    N = input()

    A = map(int, raw_input().split()).sorted()
    print A[-2]

if __name__ == '__main__':
    main()

