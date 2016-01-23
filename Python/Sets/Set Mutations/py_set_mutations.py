def main():
    A = input()
    setA = set(raw_input().split())
    N = input()

    for n in xrange(N):
        command = raw_input().split()[0]

        if command == "intersection_update":
            setA &= set(raw_input().split())
        if command == "difference_update":
            setA -= set(raw_input().split())
        if command == "symmetric_difference_update":
            setA ^= set(raw_input().split())
        if command == "update":
            setA |= set(raw_input().split())

    print sum(map(int, setA))

if __name__ == '__main__':
    main()

