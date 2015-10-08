#include <stdio.h>
#include <string.h>

int main(int argc, char **argv)
{
    int hh, mm, ss;
    char period[2];

    scanf("%2d:%2d:%2d%2s", &hh, &mm, &ss, period);

    if((hh != 12) && (strcmp(period, "PM") == 0))
        hh += 12;

    if((hh == 12) && (strcmp(period, "AM") == 0))
        hh = 0;

    printf("%02d:%02d:%02d\n", hh, mm, ss);

    return 0;
}

