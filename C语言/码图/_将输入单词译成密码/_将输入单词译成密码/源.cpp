#include <stdio.h>
int main()
{
    int c[21];
    int i = 1;
    for (i = 1; i <= 20; i++)
    {
        c[i] = getchar();
        if ((c[i] >= 65 && c[i] <= 86) || (c[i] >= 97 && c[i] <= 118))
            c[i] = c[i] + 4;
        else
            if (c[i] >= 87 && c[i] <= 90 || c[i] >= 119 && c[i] <= 122)
                c[i] = c[i] - 22;
            else
                printf("error");
        printf("%c", c[i]);

    }
    return 0;
}