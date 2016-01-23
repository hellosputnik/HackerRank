def main():
    N = input()

    L = []
    for n in xrange(N):
        commands = raw_input().split()
        command = commands[0]

        if command == "append":
            L.append(int(commands[1]))
        if command == "insert":
            L.insert(int(commands[1]), int(commands[2]))
        if command == "pop":
            L.pop()
        if command == "print":
            print L
        if command == "remove":
            L.remove(int(commands[1]))
        if command == "reverse":
            L.reverse()
        if command == "sort":
            L.sort()

if __name__ == '__main__':
    main()

