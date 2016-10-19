import re

def main():
    N = input()

    text = []
    for n in xrange(N):
        line = raw_input()
        text.append(line)

    for line in text:
        print re.sub("(?<= )\&\&(?= )", "and", re.sub("(?<= )\|\|(?= )", "or", line))

if __name__ == '__main__':
    main()

