#include<stdio.h>
#include <string.h>
#pragma warning(disable : 4996)
#define MAX(a,b) (a>b)? a : b
int main()
{
	int x, y, z;
	scanf("%d,%d,%d", &x, &y, &z);
	x = MAX(x, y);
	x = MAX(x, z);
	printf("%d", x);
	return 0;
}