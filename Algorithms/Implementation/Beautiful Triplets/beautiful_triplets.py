def main():
    n, d = map(int, raw_input().split())
    sequence = map(int, raw_input().split())

    triplets = 0
    for number in sequence:
        if number + d in sequence and number + 2 * d in sequence:
            triplets += 1

    print triplets


if __name__ == '__main__':
    main()

