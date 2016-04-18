def main():
    N = input()

    addresses = []
    for n in xrange(N):
        addresses.append(raw_input())

    # Correct format
    addresses = filter(lambda x: x.find("@") > 0, addresses)
    addresses = filter(lambda x: x.find("@") < x.find(".") and x.find("@") + 1 != x.find("."), addresses)
    addresses = filter(lambda x: x.count(".") == 1 and x.count("@") == 1, addresses)

    # Correct username
    addresses = filter(lambda x: reduce(lambda a, b: a and True if b.isalnum() or b == "-" or b == "_" else False, x[:x.find("@")]), addresses)

    # Correct website
    addresses = filter(lambda x: reduce(lambda a, b: a and True if b.isalnum() else False, x[x.find("@") + 1:x.find(".")]), addresses)

    # Length of extension is 3
    addresses = filter(lambda x: x[-4] == "." or x[-3] == "." or x[-2] == ".", addresses)

    print sorted(addresses)

if __name__ == '__main__':
    main()

