#include <stdio.h>
#pragma warning(disable : 4996)
int main()
{
	int c[50];
	int i = 0;
	int j = 0;
	char zim;

	for (j = 0; (c[j] = getchar()) != '\n'; j++);
	while (i <= (j - i - 1)) 
	{
		zim = c[i];
		c[i] = c[j - 1 - i];
		c[j - 1 - i] = zim;
	    

		i++;
	}
    for (i = 0; i <= (j - 1); i++)
			printf("%c", c[i]);
	return 0;
}

