#include <stdio.h>

int main(int argc, char **argv)
{
    int N;

    scanf("%d", &N);
    for(int n = 1; n <= N; ++n)
    {
        int i;

        for(i = 0; i < (N - n); ++i)
            printf(" ");

        for(i = (N - n); i < N; ++i)
            printf("#");

        printf("\n");
    }

    return 0;
}

