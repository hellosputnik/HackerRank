import re

def validate(CCN):
    # Must starts with 4, 5, or 6
    if not re.search("^[456].*", CCN):
        return False

    # Must contains exactly 16 digits
    if not re.search("([\d]-?){16}", CCN):
        return False

    # May contain hyphens after every 4 numbers
    if not re.search("^[\d]{4}-[\d]{4}-[\d]{4}-[\d]{4}$|^[\d]{4}[\d]{4}[\d]{4}[\d]{4}$", CCN):
        return False

    # Must not contain 4 or more consecutive, repeated integers
    if re.search(r"([\d])-?\1-?\1-?\1", CCN):
        return False

    return True


def main():
    N = input()

    for n in xrange(N):
        CCN = raw_input()
        print "Valid" if validate(CCN) else "Invalid"


if __name__ == '__main__':
    main()

