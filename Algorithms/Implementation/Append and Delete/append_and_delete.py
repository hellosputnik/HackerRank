def f(s, t, k):
    length = min(len(s), len(t))

    common = 0
    for index in xrange(length):
        if s[index] != t[index]:
            break
        common += 1

    deletions = (len(s) - common)
    result = ((k - deletions) - (len(t) - common))

    if result < 0:
        return False
    if result == 0:
        return True
    if result % 2 == 0:
        return True
    if result > len(s) + len(t) or k > len(s) + len(t):
        return True

    return False


def main():
    s = raw_input()
    t = raw_input()
    k = input()

    if f(s, t, k):
        print "Yes"
    else:
        print "No"


if __name__ == '__main__':
    main()

