#include <stdio.h>
#include <stdlib.h>


int main(int argc, char **argv) {
    int n;
    int *score;

    scanf("%d\n", &n);
    score = malloc(sizeof(int) * n);

    int highestScore;
    int lowestScore;

    scanf("%d", &score[0]);
    highestScore = lowestScore = score[0];

    int numberOfTimes [] = {0, 0};

    for (int game = 1; game < n; ++game) {
        scanf("%d", &score[game]);

        if (score[game] > highestScore) {
            highestScore = score[game];
            ++numberOfTimes[0];
            continue;
        }

        if (score[game] < lowestScore) {
            lowestScore = score[game];
            ++numberOfTimes[1];
            continue;
        }

        // There is no equal case.
    }

    printf("%d %d\n", numberOfTimes[0], numberOfTimes[1]);

    return 0;
}

