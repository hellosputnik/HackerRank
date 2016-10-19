def decorator(func):
    def standardized_func(numbers):
        standardized_numbers = ["+91 " + number[-10:-5] + " " + number[-5:] for number in numbers]
        return func(standardized_numbers)
    return standardized_func

def main():
    N = input()

    numbers = []
    for n in xrange(N):
        number = raw_input()
        numbers.append(number)

    decorated_sort = decorator(sorted)

    for number in decorated_sort(numbers):
        print number


if __name__ == '__main__':
    main()

