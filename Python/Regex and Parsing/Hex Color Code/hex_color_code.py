import re

def main():
    N = input()

    body = False
    for n in xrange(N):
        line = raw_input()

        results = re.findall("(\#[0-9A-F]{6}|\#[0-9A-F]{3})", line, flags=re.I)
        if results and body:
            for result in results:
                print result

        if "{" in line:
            body = True
        if "}" in line:
            body = False

if __name__ == '__main__':
    main()

