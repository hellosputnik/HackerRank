import collections


def main():
    n = input()
    A = map(int, raw_input().split())

    counter = collections.Counter(A)
    print (len(A) - counter.most_common(1)[0][1])


if __name__ == '__main__':
    main()

