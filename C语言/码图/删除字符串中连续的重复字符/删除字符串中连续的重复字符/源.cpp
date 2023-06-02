#include<stdio.h>
#include<string.h>
int main()
{
	int a, i = 0;
	char c[50];
	gets_s(c);
	a = strlen(c);
	for (i = 0; i < a; i++)
	{
		if ((c[i] == c[i + 1]) && ((c[i] < '0' )||( c[i]>'9' && c[i] < 'A') || (c[i]>'Z' && c[i] < 'a'||c[i]>'z')))
			c[i] = ' ';
	}
	for (i = 0; i <= a; i++)
	{
		if (c[i] != ' ')
			printf("%c", c[i]);
	}
	return 0;
}