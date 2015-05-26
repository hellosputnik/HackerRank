def diff(A, B):
    difference = 0

    for each in set(A.join(B)):
        difference += abs(A.count(each) - B.count(each))

    return difference

def main():
    A, B = raw_input(), raw_input()

    print diff(A, B)

if __name__ == '__main__':
    main()

