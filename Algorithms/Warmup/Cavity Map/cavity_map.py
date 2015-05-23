def check(square, x, y):
    value = square[x][y]
    
    if value <= square[x + 1][y]:
        return False
    if value <= square[x - 1][y]:
        return False
    if value <= square[x][y + 1]:
        return False
    if value <= square[x][y - 1]:
        return False

    return True

def main():
    n = input()
    
    cavities, square = [], []
    for each in xrange(n):
        square.append(map(int, list(str(input()))))

    for y, row in enumerate(square):
        if y == 0 or y == (len(square) - 1):
            continue
        for x, column in enumerate(row):
            if x == 0 or x == (len(row) - 1):
                continue
            if check(square, x, y):
                cavities.append((y, x))

    for each in cavities:
        square[each[0]][each[1]] = 'X'
    
    for each in square:
        each = map(str, each)
        print ''.join(each)

if __name__ == '__main__':
    main()

