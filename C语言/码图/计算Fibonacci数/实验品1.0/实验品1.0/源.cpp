#pragma warning(disable : 4996)
#include<stdio.h>
int main() {
	char c[21];
	int len = 1, i;
	do
	{
		c[len] = getchar();
		if (((c[len] < 65 || (c[len] > 90 && c[len] < 97) || c[len]>122) && c[len] != 10) || c[1] == 10)
		{
			printf("error\n");
			return 0;
		}
		len++;
	} while (c[len - 1] != 10 && len <= 20);
	for (i = 1; i < len; i++)
	{
		c[i] += 4;
		if ((c[i] > 90 && c[i] < 97) || c[i] > 122)
		{
			c[i] -= 26;
		}
		if (c[i] != 14)
		{
			printf("%c", c[i]);
		}
	}
	return 0;
}