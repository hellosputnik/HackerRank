def main():
    e = input()
    E = set(raw_input().split())
    f = input()
    F = set(raw_input().split())

    print len(E.difference(F))

if __name__ == '__main__':
    main()

