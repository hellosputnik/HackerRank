def main():
    n = input()
    s = set(map(int, raw_input().split()))
    N = input()

    for _ in xrange(N):
        commands = raw_input().split()

        if commands[0] == "discard":
            s.discard(int(commands[1]))
        if commands[0] == "pop":
            s.pop()
        if commands[0] == "remove":
            s.remove(int(commands[1]))

    print sum(s)

if __name__ == '__main__':
    main()

