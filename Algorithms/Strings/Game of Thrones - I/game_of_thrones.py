import collections

def check(string):
    dictionary = collections.defaultdict(int)

    for character in string:
        dictionary[character] ^= 1

    if len(string) % 2:
        return "YES" if sum(dictionary.values()) <= 1 else "NO"
    else:
        return "YES" if sum(dictionary.values()) == 0 else "NO"

def main():
    string = raw_input()
    print check(string)

if __name__ == '__main__':
    main()

