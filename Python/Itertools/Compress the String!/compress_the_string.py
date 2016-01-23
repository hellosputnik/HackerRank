import itertools

def main():
    S = raw_input()

    for x, group in itertools.groupby(S):
        print (len(list(group)), int(x)),

if __name__ == '__main__':
    main()

