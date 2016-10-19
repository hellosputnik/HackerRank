import re

def main():
    S = raw_input()

    if re.search(r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$", S):
        print True
    else:
        print False

if __name__ == '__main__':
    main()

