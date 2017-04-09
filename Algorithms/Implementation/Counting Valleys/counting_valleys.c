#include <stdio.h>


int main(int argc, char **argv) {
    int n;

    scanf("%d\n`", &n);

    char direction = ' ';
    int level = 0;
    int valleys = 0;

    for (int i = 0; i < n; ++i) {
        char step;

        scanf("%c", &step);

        switch (step) {
            case 'D':
                if (level == 0)
                    ++valleys;
                --level;
                break;
            case 'U':
                ++level;
                break;
            default:
                break;
        }
    }

    printf("%d\n", valleys);

    return 0;
}

