read N;

echo '
import sys

def main():
    N = int(sys.argv[1])
    COLUMNS = 100
    ROWS = 63
    matrix = [["_" for column in xrange(COLUMNS)] for row in xrange(ROWS)]

    draw(matrix, N, COLUMNS/2-1, ROWS)

    display(matrix)


def display(matrix):
    for row in matrix:
        print "".join(row)


def draw(matrix, N, x, y, size=32):
    if N == 0:
        return

    for row in reversed(xrange(y - size / 2 + 1, y)):
        matrix[row][x] = "1"

    offset = 0
    for row in reversed(xrange(y - size, y - size / 2 + 1)):
        matrix[row][x + offset] = "1"
        matrix[row][x - offset] = "1"
        offset += 1

    offset -= 1
    draw(matrix, N - 1, x + offset, y - size, size / 2)
    draw(matrix, N - 1, x - offset, y - size, size / 2)

if __name__ == "__main__":
    main()
' > solution.py;

# Fuck the police
python solution.py $N; rm solution.py;
