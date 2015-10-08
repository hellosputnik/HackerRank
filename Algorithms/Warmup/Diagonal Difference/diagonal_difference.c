#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv)
{
    int N, **A, first, second, difference;

    scanf("%d", &N);

    A = malloc(sizeof(int*) * N);
    for(int row = 0; row < N; ++row)
    {
        A[row] = malloc(sizeof(int) * N);
        for(int column = 0; column < N; ++column)
        {
            scanf("%d", &A[row][column]);
        }
    }

    first = 0, second = 0;
    for(int n = 0; n < N; ++n)
    {
        first += A[n][n];
        second += A[n][N - n - 1];
    }

    difference = abs(first - second);
    printf("%d\n", difference);

    return 0;
}

