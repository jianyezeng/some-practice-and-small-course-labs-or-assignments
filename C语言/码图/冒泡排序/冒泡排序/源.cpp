#include<stdio.h>
#pragma warning(disable : 4996)
int main()
{
	int i = 0;
	int t = 0;
	int j = 0;
	int num[10];
	for (i=0; i < 10; i++)
		scanf("%d", &num[i]);
	for (j = 0; j < 10;j++)
	{
		for (i = 0; i < 9 - j; i++)
			if (num[i] > num[i + 1])
			{
				t = num[i + 1];

				num[i + 1] = num[i];
				num[i] = t;
			}
	}
	for (i = 0; i < 10; i++)
		printf("%d,", num[i]);
	return 0;
}