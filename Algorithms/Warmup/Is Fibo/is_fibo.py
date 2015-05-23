def fibonacci(N):
    while fibonacci.n < N:
        fibonacci.n = int(round(fibonacci.n * 1.6180339887))
        fibonacci.numbers.append(fibonacci.n)
    return fibonacci.numbers

def is_fibo(N):
    numbers = fibonacci(N)

    if N in numbers:
        return "IsFibo"
    else:
        return "IsNotFibo"

def main():
    T = input()

    fibonacci.n, fibonacci.numbers = 1, [1]
    for t in xrange(T):
        N = input()
        print is_fibo(N)

if __name__ == '__main__':
    main()

