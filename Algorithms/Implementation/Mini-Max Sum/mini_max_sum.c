#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv)
{
    long long *numbers = (long long*)malloc(sizeof(long long) * 5);

    long long min = 1000000000;
    long long max = 1;
    long long sum = 0;

    for(int i = 0; i < 5; ++i)
    {
        scanf("%lld ", &numbers[i]);

        if(numbers[i] > max)
            max = numbers[i];
        if(numbers[i] < min)
            min = numbers[i];

        sum += numbers[i];
    }

    printf("%lld %lld", (sum - max), (sum - min));

    return 0;
}

