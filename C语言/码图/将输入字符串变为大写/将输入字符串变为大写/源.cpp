#include <stdio.h>
int main()
{
	int i = 1;
	int c[21];
	for (i = 1; i <= 20; i++)
	{
		c[i] = getchar();
		if (c[i] >= 97 && c[i] <= 122)
		{
			c[i] = c[i] - 32;
			printf("%c", c[i]);
		}
		else
			printf("%c", c[i]);
	}
	return 0;
}