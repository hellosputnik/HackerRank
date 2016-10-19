import re

def main():
    S = raw_input()

    for s in re.split("[,|\.]", S):
        if s:
            print s

if __name__ == '__main__':
    main()

