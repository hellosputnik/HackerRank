#include <stdio.h>


int main(int argc, char **argv) {
    int n;
    int height;

    scanf("%d", &n);

    if (n <= 0)
        return 1;

    int numberOfCandles = 0;
    int maxHeight = 0;

    for (int i = 0; i < n; ++i) {
        scanf("%d", &height);

        if (height == maxHeight)
            ++numberOfCandles;

        if (height > maxHeight) {
            numberOfCandles = 1;
            maxHeight = height;
        }
    }

    printf("%d\n", numberOfCandles);

    return 0;
}

