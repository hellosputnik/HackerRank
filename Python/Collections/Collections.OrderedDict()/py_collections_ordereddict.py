import collections

def main():
    N = input()

    items = collections.OrderedDict()

    for n in xrange(N):
        line = raw_input()

        name, price = " ".join(line.split()[:-1]), int(line.split()[-1:][0])
        if name in items:
            items[name] += price
        else:
            items[name] = price

    for item in items:
        print item, items[item]

if __name__ == '__main__':
    main()

