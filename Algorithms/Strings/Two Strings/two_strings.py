import difflib

def main():
    T = input()

    for t in xrange(T):
        A, B = raw_input(), raw_input()
        diff = difflib.SequenceMatcher(None, A, B, False)
        print "YES" if diff.quick_ratio() else "NO"

if __name__ == '__main__':
    main()

