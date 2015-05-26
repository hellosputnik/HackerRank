def permute(word):
    index = len(word) - 1
    while index > 0 and word[(index - 1)] >= word[index]:
        index -= 1
    if index <= 0:
        return "no answer"

    swap = len(word) - 1
    while word[swap] <= word[(index - 1)]:
        swap -= 1
    word[(index - 1)], word[swap] = word[swap], word[(index - 1)]

    word[index:] = word[(len(word) - 1):(index - 1):-1]

    return ''.join(word)

def main():
    t = input()

    for case in xrange(t):
        w = raw_input()
        print permute(list(w))

if __name__ == '__main__':
    main()

