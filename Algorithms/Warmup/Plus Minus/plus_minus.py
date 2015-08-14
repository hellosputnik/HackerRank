def main():
    N = input()
    A = map(int, raw_input().split())

    zero, positive, negative = 0, 0, 0
    for a in A:
        if a > 0:
            positive += 1
        elif a < 0:
            negative += 1
        else:
            zero += 1

    total = float(len(A))

    print "%.3f\n%.3f\n%.3f\n" % ((positive / total), (negative / total), (zero / total))

if __name__ == '__main__':
    main()

