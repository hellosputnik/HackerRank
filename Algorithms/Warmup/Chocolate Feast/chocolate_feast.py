def calculate(N, C, M):
    return ((N / C) + ((N / C) - 1) / (M - 1))

def main():
    T = input()
    
    for t in xrange(T):
        N, C, M   = map(int, raw_input().split())
        print calculate(N, C, M)

if __name__ == '__main__':
    main()

