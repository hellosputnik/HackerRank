#include <stdio.h>


#define min(x, y) x < y ? x : y


int calculate(int n, int p) {
    return min((p / 2), (n - p) / 2);
}

int main(int argc, char **argv) {
    int n;
    int p;

    scanf("%d", &n);
    scanf("%d", &p);

    printf("%d", calculate(n, p));

    return 0;
}

