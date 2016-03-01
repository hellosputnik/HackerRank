import collections

def main():
    T = input()

    for t in xrange(T):
        n = input()
        cubes = collections.deque(map(int, raw_input().split()))

        stack = []

        while len(cubes):
            if cubes[0] > cubes[-1]:
                if len(stack) == 0:
                    stack.append(cubes[0])
                    cubes.popleft()
                elif stack[-1] >= cubes[0]:
                    stack.append(cubes[0])
                    cubes.popleft()
                else:
                    break
            else:
                if len(stack) == 0:
                    stack.append(cubes[-1])
                    cubes.pop()
                elif stack[-1] >= cubes[-1]:
                    stack.append(cubes[-1])
                    cubes.pop()
                else:
                    break

        if len(cubes):
            print "No"
        else:
            print "Yes"

if __name__ == '__main__':
    main()

