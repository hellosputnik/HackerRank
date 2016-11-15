#include <stdio.h>
#include <stdlib.h>

// Rotate the array once
void rotate(int*, int);

// Rotate the array an arbitrary amount of times
void rotates(int*, int, int);

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

    rotates(a, n, k);

    for(int i = 0; i < q; ++i)
    {
        int m;
        scanf("%d", &m);

        printf("%d\n", a[m]);
    }

    return 0;
}

// Rotate the array by moving each element one position to the right. The
// process begins from the end and execute backwards.
void rotate(int *array, int size)
{
    int last_element = *(array + size - 1);

    while(size--)
        array[size] = array[(size - 1)];

    array[0] = last_element;
}

// Rotate the array x-amount of times by calling rotate() x-amount of times.
// TODO: Optimize this algorithm
void rotates(int *array, int size, int rotations)
{
    rotations = rotations % size;

    while(rotations--)
    {
        rotate(array, size);
    }
}

