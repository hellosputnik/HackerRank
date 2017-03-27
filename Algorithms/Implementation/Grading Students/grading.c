#include <stdio.h>

int main(int argc, char **argv) {
    // n is the number of students.
    int n = 0;

    // Get the number of students.
    scanf("%d", &n);

    // Read the grades for each student.
    for (int i = 0; i < n; ++i) {
        int grade;
        int counter;

        // Read in the grade for the i-th student.
        scanf("%d", &grade);

        // Find the next multiple of 5 and the difference between the grade
        // and that multiple.
        counter = 0;
        while ((grade + counter) % 5 != 0)
            ++counter;

        // Is the grade eligible for rounding?
        if (counter < 3 && grade >= 38)
            // If the difference is less than 3 AND the grade is greater than or
            // equal to 38 (i.e. not less than 38), then round.
            printf("%d\n", (grade + counter));
        else
            // Otherwise, the grade is ineligible for rounding.
            printf("%d\n", grade);
    }

    return 0;
}
