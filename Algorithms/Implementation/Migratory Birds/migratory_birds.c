#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int main(int argc, char **argv) {
    int n;
    int *types;

    scanf("%d", &n);
    types = malloc(sizeof(int) * n);

    memset(types, 0, sizeof(int) * n);

    for (int i = 0; i < n; ++i) {
        int type;

        scanf("%d", &type);
        ++types[(type - 1)];
    }

    int max = 0;
    int mostCommonType = 0;

    for (int i = 0; i < n; ++i) {
        if (types[i] > max) {
            max = types[i];
            mostCommonType = (i + 1);
        }
    }

    printf("%d", mostCommonType);

    return 0;
}

// This code is not optimized. It is O(2n), but it can be O(n) with the use of
// a sorted data structure.

