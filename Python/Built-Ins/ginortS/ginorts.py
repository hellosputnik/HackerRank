def main():
    S = raw_input()

    print reduce(lambda x, y: (x + y), sorted(S, key=lambda x: (x.isdigit(), x.isdigit() and not int(x) % 2, x.isupper(), x.islower(), x)))

if __name__ == '__main__':
    main()

