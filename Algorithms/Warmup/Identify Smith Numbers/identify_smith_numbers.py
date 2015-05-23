from math import sqrt

def factor(x):
    return sorted(reduce(list.__iadd__, [[n, x / n] for n in range(1, int(sqrt(x)) + 1) if not (x % n)]))    

def is_prime(x):
    return True if len(factor(x)) == 2 else False

def prime_factor(x):

    if is_prime(x):
        return [x]

    factors = factor(x)[1:-1]

    prime_factors = []
    while x != 1:
        for each in factors:
            if is_prime(each) and x % each == 0:
                prime_factors.append(each)
                x /= each

    return prime_factors

def smith(number):
    digits  = sum(map(int, list(str(number))))
    factors = sum(map(int, reduce(list.__iadd__, map(list, map(str, prime_factor(number))))))
    
    return 1 if digits == factors and number != 1 else 0

def main():
    N = input()

    print smith(N)

if __name__ == '__main__':
    main()

