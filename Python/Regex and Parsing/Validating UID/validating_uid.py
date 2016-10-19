import re

def validate(UID):
    # Should contain at least 2 uppercase English
    if not re.search("([A-Z].*){2,}", UID):
        return False

    # Should contain at least 3 digits
    if not re.search("([0-9].*){3,}", UID):
        return False

    # Should contain only alphanumeric characters AND exactly 10 characters
    if not re.search("([a-zA-Z0-9]){10}", UID):
        return False

    # Should not contain repeating characters
    if re.search(r"(.).*\1", UID):
        return False

    return True


def main():
    T = input()

    for t in xrange(T):
        UID = raw_input()
        print "Valid" if validate(UID) else "Invalid"

if __name__ == '__main__':
    main()

