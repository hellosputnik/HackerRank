import collections


def happy(board):
    if board.count("_") == 0:
        index = 0

        while index < len(board):
            char  = board[index]
            happy = False

            if (index + 1) < len(board) and char == board[(index + 1)]:
                happy = True
            else:
                return False

            while index < len(board) and board[index] == char:
                index += 1

        return True
    else:
        counter = collections.Counter(board)
        for each in counter:
            if each != "_" and counter[each] == 1:
                return False

        return True


def main():
    g = input()

    for game in xrange(g):
        n = input()
        b = raw_input()

        print "YES" if happy(b) else "NO"


if __name__ == '__main__':
    main()

