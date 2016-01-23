def main():
    S = raw_input()

    functions = [str.isalnum, str.isalpha, str.isdigit, str.islower, str.isupper]

    for f in functions:
        result = False
        for s in S:
            result |= f(s)
        print result

if __name__ == '__main__':
    main()

