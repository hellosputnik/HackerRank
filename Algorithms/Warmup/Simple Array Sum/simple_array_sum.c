#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv)
{
    int N, *A, sum;

    scanf("%d", &N);
    A = malloc(sizeof(int) * N);

    sum = 0;
    for(int n = 0; n < N; ++n)
    {
        scanf("%d", &A[n]);
        sum += A[n];
    }

    free(A);
    printf("%d\n", sum);

    return 0;
}

