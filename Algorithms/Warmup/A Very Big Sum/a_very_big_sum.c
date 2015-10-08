#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv)
{
    int N;

    long long *A, sum;

    scanf("%d", &N);
    A = malloc(sizeof(int) * N);

    sum = 0;
    for(int n = 0; n < N; ++n)
    {
        scanf("%lld", &A[n]);
        sum += A[n];
    }

    free(A);
    printf("%lld\n", sum);

    return 0;
}

