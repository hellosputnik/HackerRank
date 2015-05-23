def pi(song):
    PI = "31415926535897932384626433833"

    for index, word in enumerate(song.split()):
        if len(word) != int(PI[index]):
            return "It's not a pi song."

    return "It's a pi song."

def main():
    T = input()

    for t in xrange(T):
        print pi(raw_input())

if __name__ == '__main__':
    main()

