def insertionSort(array):
    shifts = 0
    for j in xrange(1, len(array)):
        key = array[j]
        i = j - 1
        while i >= 0 and array[i] > key:
            array[(i + 1)] = array[i]
            i = i - 1
            shifts += 1
        array[(i + 1)] = key

    return shifts

def main():
    s = input()
    ar = map(int, raw_input().split())

    print insertionSort(ar)

if __name__ == '__main__':
    main()

