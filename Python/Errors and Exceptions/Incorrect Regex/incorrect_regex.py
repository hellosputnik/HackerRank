import re

def main():
    T = input()

    for t in xrange(T):
        pattern = raw_input()

        try:
            re.compile(pattern)
            print True
        except re.error:
            print False

if __name__ == '__main__':
    main()

