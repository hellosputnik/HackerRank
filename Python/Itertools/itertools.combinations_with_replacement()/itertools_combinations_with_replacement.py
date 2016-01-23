import itertools

def main():
    S, k = raw_input().split()

    S, k = sorted(S), int(k)
    for each in itertools.combinations_with_replacement(S, k):
        print ''.join(each)

if __name__ == '__main__':
    main()

