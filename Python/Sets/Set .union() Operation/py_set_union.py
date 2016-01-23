def main():
    n = input()
    English = set(raw_input().split())
    b = input()
    French = set(raw_input().split())

    print len(English.union(French))

if __name__ == '__main__':
    main()

