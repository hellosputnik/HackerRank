import collections


def main():
    n = input()
    c = map(int, raw_input().split())

    inventory = collections.Counter(c)
    pairs = 0
    for item in inventory:
        pairs += (inventory[item] / 2)
    print pairs


if __name__ == '__main__':
    main()

