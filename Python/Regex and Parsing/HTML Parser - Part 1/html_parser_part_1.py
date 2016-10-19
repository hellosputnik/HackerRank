from HTMLParser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print "Start :", tag
        for attr in attrs:
            print "->", attr[0], ">", attr[1]
    def handle_endtag(self, tag):
        print "End   :", tag
    def handle_startendtag(self, tag, attrs):
        print "Empty :", tag
        for attr in attrs:
            print "->", attr[0], ">", attr[1]


def main():
    N = input()

    lines = []
    for n in xrange(N):
        line = raw_input()
        lines.append(line)

    parser = MyHTMLParser()
    parser.feed("\n".join(lines))


if __name__ == '__main__':
    main()

