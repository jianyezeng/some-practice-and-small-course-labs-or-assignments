#include<stdio.h>
#include<string.h>
int main()
{
	char c[256];
	int i, num = 0;
	int word = 0;
	gets_s(c);
	int a = strlen(c);
	for (i = 0; i < a; i++)
	{
		if (c[i] == ' ')
			word = 0;
		else {
			if (word == 0)
			{
				num++;
				word = 1;
			}
			else
				word = 1;

		}
	}
	printf("%d", num);
	return 0;
}