def alternate(string):
    mode = string[0]

    delete = 0
    for character in string[1:]:
        if character == mode:
            delete += 1
        else:
            mode = character

    return delete

def main():
    T = input()

    for t in xrange(T):
        string = raw_input()
        print alternate(string)

if __name__ == '__main__':
    main()

