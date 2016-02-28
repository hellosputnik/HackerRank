import itertools

def main():
    N, letters, K = input(), raw_input().split(), input()

    groups = list(itertools.combinations(letters, K))

    print sum([1.0 for group in groups if 'a' in group]) / len(groups)

if __name__ == '__main__':
    main()

