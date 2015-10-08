def function(x):
    for element in x:
        if x.count(element) > 1:
            return "NO"
    return "YES"

def main():
    n = input()
    y = map(int, raw_input().split())

    print function(y)

if __name__ == '__main__':
    main()

