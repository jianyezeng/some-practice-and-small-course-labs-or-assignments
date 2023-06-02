#include <stdio.h>
void my_strcat(char* destination, const char* source);
int main()
{
    char a[100],b[100];
    gets_s(a);
    gets_s(b);
    my_strcat(b, a);
}
void my_strcat(char* destination, const char* source)
{
    int i = 0;
    int n;
    if (destination == NULL || source == NULL)
        printf("error");
    else
    {
        while (*(source + i) != '\0')
        {
            *(destination + i) = *(source + i);
            i++;
        }
    }
    for (n = 0; n < i; n++)
        printf("%s", source + i);
}