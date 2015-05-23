def decent_number(N):

    if N < 3:
        return -1

    remainder = N % 3

    if remainder == 0:
        return '5' * N
    if remainder == 1:
        return ('5' * (N - 10)) + ('33333' * 2) if N >= 10 else -1
    if remainder == 2:
        return ('555' * ((N / 3) - 1)) + '33333'

    return -1

def main():
    T = input()
    
    for t in xrange(T):
        N = input()
        print decent_number(N)

if __name__ == '__main__':
    main()

