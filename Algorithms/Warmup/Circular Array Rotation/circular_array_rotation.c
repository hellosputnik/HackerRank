#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Rotate the array an arbitrary amount of times
void rotate(int*, int, int);

int main(int argc, char **argv)
{
    int n, k, q;
    scanf("%d %d %d", &n, &k, &q);

    int *a;
    a = (int*)malloc(sizeof(int) * n);

    for(int i = 0; i < n; ++i)
    {
        int element;
        scanf("%d", &element);

        a[i] = element;
    }

    rotate(a, n, k);

    for(int i = 0; i < q; ++i)
    {
        int m;
        scanf("%d", &m);

        printf("%d\n", a[m]);
    }

    return 0;
}

// Rotate the array by moving each element a specified amount to the right. The
// process begins from the end and execute backwards.
void rotate(int *array, int size, int rotations)
{
    // Reduce extraneous rotation cycles.
    rotations = rotations % size;

    int *saved_elements = (int*)malloc(sizeof(int) * rotations);

    // Save elements that would 'overflow'.
    memcpy(saved_elements, (array + size - rotations), sizeof(int) * rotations);

    // Rotate elements by the specified amount beginning from the end.
    for(int i = 0; i < (size - rotations); ++i)
        array[((size - 1) - i)] = array[((size - 1) - i - rotations)];

    // Insert saved elements
    memcpy(array, saved_elements, sizeof(int) * rotations);
}

