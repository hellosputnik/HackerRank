import itertools

def main():
    A = map(int, raw_input().split())
    B = map(int, raw_input().split())

    for each in itertools.product(A, B):
        print each,

if __name__ == '__main__':
    main()

