def capitalize(string):
    for each in string.split():
        string = string.replace(each, each.capitalize())

    return string

def main():
    S = raw_input()

    print capitalize(S)

if __name__ == '__main__':
    main()

