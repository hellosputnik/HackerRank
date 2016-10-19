from HTMLParser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, comments):
        if '\n' in comments:
            print ">>> Multi-line Comment"
        else:
            print ">>> Single-line Comment"
        print comments
    def handle_data(self, data):
        if data.strip():
            print ">>> Data"
            print data


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

