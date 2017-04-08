#include <stdio.h>
#include <stdlib.h>


int sum(int *array, int begin, int end) {
    int y = 0;

    for (int i = begin; i < end; ++i)
        y += array[i];

    return y;
}

int main(int argc, char **argv) {
    int n;
    int *sequence;
    int m, d;

    scanf("%d", &n);
    sequence = malloc(sizeof(int) * n);

    for (int i = 0; i < n; ++i)
        scanf("%d", &sequence[i]);

    scanf("%d %d", &d, &m);

    int count = 0;

    for (int i = 0; i <= (n - m); ++i) {
        if (sum(sequence, i, i + m) == d)
            ++count;
    }

    printf("%d\n", count);

    return 0;
}

