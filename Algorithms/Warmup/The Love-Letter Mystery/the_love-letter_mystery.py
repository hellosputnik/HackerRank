def f(x):
    result = 0

    for index, character in enumerate(x):
        result += abs(ord(character) - ord(x[-(index) - 1]))
        if index == (len(x) - 1) / 2:
            break

    return result

T = input()

for t in xrange(T):
    print f(raw_input())

