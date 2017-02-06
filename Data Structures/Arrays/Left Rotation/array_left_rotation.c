#include <stdio.h>
#include <stdlib.h>


int main(int argc, char **argv)
{
    int n, d;
    int *array;

    scanf("%d %d", &n, &d);

    array = (int*)malloc(sizeof(int) * n);
    for (int i = 0; i < n; ++i)
        scanf("%d", &array[i]);

    // Remove redundant shifts.
    d = d % n;

    // Print the left half of the shifted numbers.
    for (int i = d; i < n; ++i)
        printf("%d ", array[i]);

    // Print the right half of the shifted numbers.
    for (int i = 0; i < d; ++i)
        printf("%d ", array[i]);

    return 0;
}

