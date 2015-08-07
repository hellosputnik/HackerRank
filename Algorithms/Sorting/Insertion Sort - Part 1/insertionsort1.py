def insert(array, V):
    for index in reversed(xrange(len(array) - 1)):
        if V > array[index]:
            array[(index + 1)] = V
            break
        else:
            array[(index + 1)] = array[index]
        if index == 0 and V < array[0]:
            print ' '.join(map(str, array))
            array[0] = V
            break
        print ' '.join(map(str, array))
    return array

def main():
    s = input()
    ar = map(int, raw_input().split())

    V = ar[(len(ar) - 1)]
    print ' '.join(map(str, insert(ar, V)))

if __name__ == '__main__':
    main()

