#include<stdio.h>
#pragma warning(disable : 4996)
int main()
{
	int n,i;
	int num[10000];
	num[1] = 1;
	num[2] = 1;
	scanf("%d", &n);
	for (i = 3; i <= n;i++)
	num[i] = num[i - 1] + num[i - 2];
		printf("%d", num[n]);
		return 0;
}