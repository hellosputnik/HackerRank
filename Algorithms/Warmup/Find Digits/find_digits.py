from collections import defaultdict

def f(x):
    string = str(x)
    
    count, digits = 0, defaultdict(lambda: None)

    for digit in string:
        if digit == "0":
            continue
        if digits[digit] == None:
            digits[digit] = 0 if x % int(digit) else 1
        count += digits[digit]

    return count

T = input()

for t in xrange(T):
    N = input()
    print f(N)

