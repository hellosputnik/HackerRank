import re

def main():
    N = input()

    for n in xrange(N):
        number = raw_input()
        print "YES" if re.search(r"^[789][\d]{9}$", number) else "NO"

if __name__ == '__main__':
    main()

