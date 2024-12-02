#include <cs50.h>
#include <stdio.h>

int main(void)
{ // setiing the constants
    const char *name = "#";
    int n;
    do // do while loop to gather the height of the pyramid
    {
        n = get_int("Give me the height of the pyramid please: ");
    }
    while (n < 1);

    for (int i = 0; i < n; i++)
    {
        // Right Aligned Code to set spacing of pyramid to the right
        for (int j = 0; j < n - i - 1; j++)
        {
            printf(" ");
        }

        // Printing of blocks
        for (int j = 0; j <= i; j++)
        {
            printf("%s", name);
        }
        printf("  ");

        // Left aligned code and printing of blocks
        for (int j = i + 1; j > 0; j--)
        {
            printf("%s", name);
        }
        printf("\n"); // Sending each start to a new line
    }
}
