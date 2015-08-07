#include <stdio.h>
#include <stdbool.h>
#include <string.h>

bool palindrome(char *string)
{
    int length = strlen(string);

    for(int i = 0; i < (length / 2); ++i)
    {
        if(string[i] != string[(length - i - 1)])
        {
            printf("%c, %c\n", string[i], string[(length - i - 1)]);
            return false;
        }
    }

    return true;
}

int main(int argc, char **argv)
{
    int T;

    scanf("%d", &T);

    for(int t = 0; t < T; ++t)
    {
        int N, M;
        scanf("\n%d %d", &N, &M);

        char string[32];
        sprintf(string, "%d", N);

        if(palindrome(string))
            printf("%s is a palindrome.\n", string);
        else
            printf("%s is not a palindrome.\n", string);
    }

    return 0;
}

