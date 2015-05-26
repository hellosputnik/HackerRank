def pangram(s):
    s = s.replace(' ', '').lower()
    return "pangram" if len(set(s)) == 26 else "not pangram"

def main():
    s = raw_input()
    print pangram(s)

if __name__ == '__main__':
    main()

