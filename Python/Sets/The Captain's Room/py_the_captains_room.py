def main():
    K = input()
    rooms = map(int, raw_input().split())

    A, B = set(), set()
    for room in rooms:
        if room in A:
            B.add(room)
        else:
            A.add(room)

    print (A - B).pop()

if __name__ == '__main__':
    main()

