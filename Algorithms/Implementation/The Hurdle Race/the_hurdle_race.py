def main():
    n, k   = map(int, raw_input().split())
    height = map(int, raw_input().split())

    potions = k - max(height)

    print abs(potions) if potions < 0 else 0


if __name__ == '__main__':
    main()

