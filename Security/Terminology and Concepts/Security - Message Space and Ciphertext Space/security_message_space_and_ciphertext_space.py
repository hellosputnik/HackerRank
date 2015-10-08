def main():
    string = raw_input()

    characters = [x for x in string]
    for index, c in enumerate(characters):
        characters[index] = str((int(c) + 1) % 10)
        
    print ''.join(characters)

if __name__ == '__main__':
    main()

