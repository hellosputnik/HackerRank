import textwrap

def main():
    S = raw_input()
    w = input()

    print textwrap.fill(S, w)

if __name__ == '__main__':
    main()

