N = input()
a = map(int, raw_input().split())

while a:
    print len(a)
    smallest = min(a)
    while smallest in a:
        a.remove(smallest)

