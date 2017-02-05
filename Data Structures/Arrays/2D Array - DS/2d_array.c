#include <limits.h>
#include <stdio.h>
#include <stdlib.h>

#define ROWS    6
#define COLUMNS 6

int calculate(int array[6][6], int row, int column)
{
    int sum = 0;

    // Add the top section of the hourglass.
    sum += array[row][column];
    sum += array[row][column + 1];
    sum += array[row][column + 2];

    // Add the middle section of the hourglass.
    sum += array[row + 1][column + 1];

    // Add the bottom section of the hourglass.
    sum += array[row + 2][column];
    sum += array[row + 2][column + 1];
    sum += array[row + 2][column + 2];

    return sum;
}


int main(int argc, char **argv)
{
    // Allocate space on the stack for the 2D array and the max.
    int A[6][6];
    int max;

    // Read in the 2D array.
    for (int i = 0; i < ROWS; ++i)
        for (int j = 0; j < COLUMNS; ++j)
            scanf("%d", &A[i][j]);

    // Loop through the entire 2D array to find the max sum.
    max = INT_MIN;
    for (int i = 0; i < ROWS - 2; ++i)
    {
        for (int j = 0; j < COLUMNS - 2; ++j)
        {
            int sum = calculate(A, i, j);

            if (sum > max)
                max = sum;
        }
    }

    // Print the result.
    printf("%d\n", max);

    return 0;
}

