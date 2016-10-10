def main():
    n = input()

    if n % 2:
        print "Weird"
        return

    if n >= 2 and n <= 5:
        print "Not Weird"
        return

    if n >= 6 and n <= 20:
        print "Weird"

    if n > 20:
        print "Not Weird"


if __name__ == '__main__':
    main()

