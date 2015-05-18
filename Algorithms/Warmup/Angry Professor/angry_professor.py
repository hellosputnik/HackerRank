def main():
    T = input()
  
    for t in xrange(T):
        N, K = map(int, raw_input().split())
        a = map(int, raw_input().split())
        print "YES" if len(filter(lambda x: x <= 0, a)) < K else "NO"

if __name__ == '__main__':
    main()
