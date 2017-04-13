import itertools


def main():
    s, n, m = map(int, raw_input().split())

    kprices = map(int, raw_input().split())
    uprices = map(int, raw_input().split())

    combinations = map(sum, itertools.product(kprices, uprices))
    valid_combos = filter(lambda x: x <= s, combinations)

    print max(valid_combos) if valid_combos else -1


if __name__ == '__main__':
    main()

