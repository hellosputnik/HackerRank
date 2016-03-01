import collections

def main():
    N = input()

    d = collections.deque()

    for n in xrange(N):
        command = raw_input().split()

        if command[0] == "append":
            d.append(command[1])
        if command[0] == "pop":
            d.pop()
        if command[0] == "popleft":
            d.popleft()
        if command[0] == "appendleft":
            d.appendleft(command[1])

    for value in d:
        print value,

if __name__ == '__main__':
    main()

