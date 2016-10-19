import re

def main():
    T = input()

    for t in xrange(T):
        N = raw_input()
        print bool(re.match("^[-+]?[0-9]*\.[0-9]+$", N))

if __name__ == '__main__':
    main()

