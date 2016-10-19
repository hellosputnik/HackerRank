import re

def main():
    S, k = raw_input(), raw_input()

    matches = re.finditer("(?=(%s))" % k, S)

    results = map(lambda x: (x.start(1), x.end(1) - 1), matches)
    if results:
        for result in results:
            print result
    else:
        print (-1, -1)

if __name__ == '__main__':
    main()

