def modified_kaprekar(n):

    if n <= 10:
        if n == 1 or n == 9:
            return True
        return False
    
    square = n ** 2
    d = len(str(n))

    if len(str(square)) % 2:
        l, r = int(str(square)[:(d - 1)]), int(str(square)[(d - 1):])
    else:
        l, r = int(str(square)[:d]), int(str(square)[d:])

    print l, r

    if (l + r) == n:
        return True

    return False

def main():
    p = input()
    q = input()

    numbers = []
    for n in xrange(p, q + 1):
        if modified_kaprekar(n):
            numbers.append(n)

    if len(numbers):
        for each in numbers: 
            print each,
    else:
        print "INVALID RANGE"

if __name__ == '__main__':
    main()

