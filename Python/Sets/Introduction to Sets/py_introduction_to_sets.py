def main():
    N = input()
    heights = set(map(float, raw_input().split()))

    print (sum(heights) / len(heights))

if __name__ == '__main__':
    main()

