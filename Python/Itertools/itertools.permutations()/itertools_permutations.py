import itertools

def main():
    S, k = raw_input().split()

    for each in sorted(itertools.permutations(S, int(k))):
        print "".join(each)

if __name__ == '__main__':
    main()

