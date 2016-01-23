def main():
    N = input()

    countries = set()

    for n in xrange(N):
        countries.add(raw_input())

    print len(countries)

if __name__ == '__main__':
    main()

