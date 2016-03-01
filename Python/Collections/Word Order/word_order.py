import collections

def main():
    n = input()

    words = collections.OrderedDict()

    for _ in xrange(n):
        word = raw_input()
        if word in words:
            words[word] += 1
        else:
            words[word] = 1

    print len(words)
    for word in words:
        print words[word],

if __name__ == '__main__':
    main()

