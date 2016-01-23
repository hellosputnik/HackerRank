def mutate(string, index, character):
    return str(string[:index] + character + string[(index + 1):])

def main():
    S = raw_input()
    i, c = raw_input().split()

    print mutate(S, int(i), c)

if __name__ == '__main__':
    main()

