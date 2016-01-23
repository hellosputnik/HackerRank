def count(string, substring):
    index, occurrence = 0, 0
    while True:
        index = string.find(substring, index) + 1
        if index > 0:
            occurrence += 1
        else:
            return occurrence

def main():
    string, substring = raw_input(), raw_input()

    print count(string, substring)

if __name__ == '__main__':
    main()

