def main():
    T = input()

    for t in xrange(T):
        try:
            a, b = map(int, raw_input().split())
            print a / b
        except ZeroDivisionError as e:
            print "Error Code:", e
        except ValueError as e:
            print "Error Code:", e

if __name__ == '__main__':
    main()

