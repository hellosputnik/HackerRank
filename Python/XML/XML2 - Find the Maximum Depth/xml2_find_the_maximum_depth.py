from xml.etree.ElementTree import XMLParser

class MaxDepth:
    def __init__(self):
        self.current = 0
        self.maximum = 0
    def start(self, tag, attrib):
        self.current += 1
        if self.current > self.maximum:
            self.maximum = self.current
    def end(self, tag):
        self.current -= 1
    def data(self, data):
        pass
    def close(self):
        return self.maximum


def main():
    N = input()

    lines = []
    for n in xrange(N):
        line = raw_input()
        lines.append(line)

    parser = XMLParser(target=MaxDepth())
    parser.feed("\n".join(lines))

    print (parser.close() - 1)


if __name__ == '__main__':
    main()

