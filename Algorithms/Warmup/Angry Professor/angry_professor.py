def cancelled(K, a):
    return "YES" if len(filter(lambda x: x <= 0, a)) < K else "NO"

def main():
    T = input()
  
    for t in xrange(T):
        N, K = map(int, raw_input().split())
        a = map(int, raw_input().split())
        print cancelled(K, a)

if __name__ == '__main__':
    main()

