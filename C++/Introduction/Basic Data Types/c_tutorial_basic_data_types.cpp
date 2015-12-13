#include <iostream>

int main(int argc, char **argv)
{
    int i;
    long l;
    long long ll;
    char c;
    float f;
    double d;

    scanf("%d %ld %lld %c %f %lf", &i, &l, &ll, &c, &f, &d);

    printf("%d\n", i);
    printf("%ld\n", l);
    printf("%lld\n", ll);
    printf("%c\n", c);
    printf("%f\n", f);
    printf("%lf\n", d);

    return 0;
}

