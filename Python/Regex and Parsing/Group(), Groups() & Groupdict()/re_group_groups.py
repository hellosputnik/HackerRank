import re

def main():
    S = raw_input()

    result = re.search(r"([^\W_])\1+", S)

    if result:
        print result.group(1)
    else:
        print -1

if __name__ == '__main__':
    main()

