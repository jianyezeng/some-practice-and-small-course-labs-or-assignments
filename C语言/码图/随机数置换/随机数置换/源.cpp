#include<stdio.h>
#pragma warning(disable : 4996) 
int num;
char A[1001];
int Used[1001];
extern int RandInt(int i, int j);
void RandomPermutation1(int n);
void RandomPermutation2(int n);
void RandomPermutation3(int n);
int main()
{
	int n;
	scanf("%d", &n);
	RandomPermutation3(n);
	RandomPermutation1(n);
	RandomPermutation2(num);
	for (int i = 1; i <= n; i++)
	{
		printf("%d,", A[i]);
	}
	printf("0");
}
void RandomPermutation1(int n)
{
	num = RandInt(0, n);
	int i;
	for (i = 1; i <= n; i++)
	{
		if (Used[num] != 1)
			A[i] = num;
	}
}
void RandomPermutation2(int num)
{
	Used[num] = 1;
}
void RandomPermutation3(int n)
{
	for (int i = 0; i <= n; i++)
		A[i] = i + 1;
	
}