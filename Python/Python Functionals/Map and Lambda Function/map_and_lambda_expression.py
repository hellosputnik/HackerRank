def Fibonacci(N):
    if N == 1:
        return [0]
    if N == 2:
        return [0, 1]

    result = [0, 1]

    while len(result) < N:
        result.append(result[-2] + result[-1])

    return result

def main():
    N = input()

    if N:
        print map(lambda x: x ** 3, Fibonacci(N))
    else:
        print "[]"

if __name__ == '__main__':
    main()

