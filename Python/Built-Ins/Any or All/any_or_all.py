def main():
    N, integers = input(), map(int, raw_input().split())

    positive = not any(filter(lambda x: x < 1, integers))
    palindrome = any(filter(lambda x: x < 10 or x % 11 == 0, integers))

    print all([positive, palindrome])

if __name__ == '__main__':
    main()

