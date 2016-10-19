import email.utils
import re

def validate(email_address):
    return bool(re.match("^[a-zA-Z][\w\-.]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$", email_address))


def main():
    n = input()

    for i in xrange(n):
        line = raw_input()
        name, email_address = email.utils.parseaddr(line)
        if validate(email_address):
            print email.utils.formataddr((name, email_address))


if __name__ == '__main__':
    main()

