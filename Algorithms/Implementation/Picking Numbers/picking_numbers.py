#!/usr/bin/env python3

import collections


def main():
    n = int(input())
    a = map(int, input().split())

    answer  = 0
    numbers = collections.Counter(a)

    for number in numbers:
        answer = max(answer, numbers[number - 1] + numbers[number])
        answer = max(answer, numbers[number] + numbers[number + 1])

    print(answer)


if __name__ == '__main__':
    main()

