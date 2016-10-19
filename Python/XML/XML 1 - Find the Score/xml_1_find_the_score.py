import xml.etree.ElementTree as ElementTree

def main():
    N = input()

    lines = []
    for n in xrange(N):
        line = raw_input()
        lines.append(line)

    root = ElementTree.fromstring("\n".join(lines))

    score = 0
    for it in root.iter():
        score += len(it.attrib)
    print score


if __name__ == '__main__':
    main()

