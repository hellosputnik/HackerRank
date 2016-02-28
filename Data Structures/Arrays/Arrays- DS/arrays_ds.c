#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv)
{
    int N;
    int *A;

    scanf("%d", &N);
    A = malloc(sizeof(int) * N);

    for(int n = 0; n < N; ++n)
        scanf("%d", &A[n]);

    for(int i = (N - 1); i >= 0; --i)
        printf("%d ", A[i]);

    return 0;
}

