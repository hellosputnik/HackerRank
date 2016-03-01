import collections

def main():
    counter = collections.Counter(raw_input())

    for c in sorted(counter.items(), key=lambda x: (-x[1], x[0]))[:3]:
        print c[1], c[0]

if __name__ == '__main__':
    main()

