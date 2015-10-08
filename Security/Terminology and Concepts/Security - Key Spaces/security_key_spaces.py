def function(x, e):
    characters = [c for c in x]

    for index, c in enumerate(characters):
        characters[index] = str((int(c) + e) % 10)

    print ''.join(characters)

def main():
    string = raw_input()
    e = input()

    function(string, e)

if __name__ == '__main__':
    main()

