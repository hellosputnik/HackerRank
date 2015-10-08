#include <stdio.h>

int main(int argc, char **argv)
{
    int T, A, B, sum;

    scanf("%d", &T);

    for(int t = 0; t < T; ++t)
    {
        scanf("%d %d", &A, &B);

        sum = A + B;
        printf("%d\n", sum);
    }

    return 0;
}

