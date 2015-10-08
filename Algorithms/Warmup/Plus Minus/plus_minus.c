#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv)
{
    int N, *A, zero, positive, negative;

    scanf("%d", &N);
    A = malloc(sizeof(int) * N);

    zero = 0, positive = 0, negative = 0;
    for(int n = 0; n < N; ++n)
    {
        scanf("%d", &A[n]);

        if(A[n] == 0)
            ++zero;
        if(A[n] > 0)
            ++positive;
        if(A[n] < 0)
            ++negative;
    }

    printf("%.3f\n", (positive / (float) N));
    printf("%.3f\n", (negative / (float) N));
    printf("%.3f\n", (zero / (float) N));

    return 0;
}

