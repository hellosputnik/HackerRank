from __future__ import print_function

def main():
    M = input()
    m = set(map(int, raw_input().split()))

    N = input()
    n = set(map(int, raw_input().split()))

    map(print, sorted(m ^ n))

if __name__ == '__main__':
    main()

