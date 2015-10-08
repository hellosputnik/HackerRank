#include <stdio.h>

int main(int argc, char **argv)
{
    int d, m, y, D, M, Y;

    scanf("%d %d %d", &d, &m, &y);
    scanf("%d %d %d", &D, &M, &Y);

    if(y < Y)
    {
        printf("0\n");
        goto exit;
    }
    if(y == Y && m < M)
    {
        printf("0\n");
        goto exit;
    }
    if(y == Y && m == M && d <= D)
    {
        printf("0\n");
        goto exit;
    }

    if(y > Y)
    {
        printf("10000\n");
        goto exit;
    }
    if(m > M)
    {
        printf("%d\n", (500 * (m - M)));
        goto exit;
    }
    printf("%d\n", (15 * (d - D)));

exit:
    return 0;
}

