def rotate(matrix, R):
    if R == 0:
        result = ""
        for row in matrix:
            result += " ".join(row)

        return result

def main():
    M, N, R = map(int, raw_input().split())

    matrix = []
    for m in xrange(M):
        matrix.append(raw_input().split())

    print rotate(matrix, (R % (M * N)))

if __name__ == '__main__':
    main()

