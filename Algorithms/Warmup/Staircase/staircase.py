def staircase(N):
    stair = ""
    for n in xrange(1, (N + 1)):
        stair += ((N - n) * " ") + (n * "#") + "\n"
    return stair

def main():
    N = input()

    print staircase(N)

if __name__ == '__main__':
    main()

