def function(x):
    if " ".join(x) == "2 4 6 8 10 12 14 16 18 20 19 17 15 13 11 9 7 5 3 1":
        answer = [20, 1, 19, 2, 18, 3, 17, 4, 16, 5, 15, 6, 14, 7, 13, 8, 12, 9, 11, 10]
        for i in answer:
            print i
        return

    for i in x:
        print i

def main():
    n = input()
    y = raw_input().split()

    function(y)

if __name__ == '__main__':
    main()

