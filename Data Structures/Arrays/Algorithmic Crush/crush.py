import collections


def main():
    N, M = map(int, raw_input().split())

    # Initialize the list of numbers and list of operations.
    # numbers  = [0 for n in xrange(N)]
    operations = [0 for n in xrange(N)]

    # Read the operations and reduce operations to a single operation per range.
    for m in xrange(M):
        a, b, k = map(int, raw_input().split())
        
        # k is valid between a - 1 and b - 1.
        operations[(a - 1)] += k
        if b != N:
            operations[b] -= k

    # Apply the operations to the list of numbers (and record the range).
    current = 0
    maximum = 0
    for index, operation in enumerate(operations):
        current += operation
        maximum = max(current, maximum)

    print maximum


if __name__ == '__main__':
    main()

