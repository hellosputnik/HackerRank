import collections

def main():
    N = input()

    students = collections.defaultdict()
    for n in xrange(N):
        line = raw_input().split()
        name = line[0]
        maths, physics, chemistry = map(float, line[1:])
        students[name] = ((maths + physics + chemistry) / 3)

    print "%0.2f" % students[raw_input()]

if __name__ == '__main__':
    main()

