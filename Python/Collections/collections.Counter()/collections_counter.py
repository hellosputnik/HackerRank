import collections

def main():
    X = input()
    sizes = map(int, raw_input().split())
    N = input()

    inventory = collections.Counter(sizes)
    
    money = 0
    for n in xrange(N):
        size, x = map(int, raw_input().split())
        if inventory[size]:
            money += x
            inventory[size] -= 1
    print money

if __name__ == '__main__':
    main()

