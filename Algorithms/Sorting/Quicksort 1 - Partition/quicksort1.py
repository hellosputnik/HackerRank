def partition(array):
    p = array[0]

    less, more = [], []

    for i in xrange(1, len(array)):
        value = array[i]
        if value < p:
            less.append(value)
        elif value > p:
            more.append(value)

    return ' '.join(map(str, (less + [p] + more)))

def main():
    n = input()
    ar = map(int, raw_input().split())

    print partition(ar)

if __name__ == '__main__':
    main()

