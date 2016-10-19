import re

v = "aeiou"
c = "qwrtypsdfghjklzxcvbnm"

def main():
    S = raw_input()

    results = re.findall(r"(?<=[%s])([%s]{2,})(?=[%s])" % (c, v, c), S, flags=re.I)

    if results:
        for result in results:
            print result
    else:
        print -1

if __name__ == '__main__':
    main()

