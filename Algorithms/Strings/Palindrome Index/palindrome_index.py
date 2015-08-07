def palindrome(string):
    length = len(string)

    for index in xrange(length):
        if string[index] != string[(length - index - 1)]:
            return False

    return True

def palindrome_index(string):
    if palindrome(string):
        return -1

    s = list(string)

    l, r = 0, (len(s) - 1)
    while l < (len(s) / 2) and r > (len(s) / 2):
        if s[(l + 1)] == s[r]:
            return l
        if s[l] == s[(r - 1)]:
            return r
        l, r = l + 1, r - 1

def main():
    T = input()

    for t in xrange(T):
        string = raw_input()
        print palindrome_index(string)

if __name__ == '__main__':
    main()

