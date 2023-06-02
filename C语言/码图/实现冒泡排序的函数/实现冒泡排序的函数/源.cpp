#include <stdio.h>
#pragma warning(disable : 4996)
int main()
{
	void  bubbleSort(int *data, int n);
	int i=0;
	int num;
	int c[10001];
	scanf("%d", &num);
	for (i = 0; i < num; i++)
		scanf("%d", &c[i]);
	bubbleSort(c,num);
	for (i=0;i<num;i++)
		printf("%d,", c[i]);
	return 0;
}
void  bubbleSort(int* data, int n)
{
	int a, b;
	int zim;
	for (a = 0; a < n; a++)
	{
		for (b = 0; b < (n-1-a); b++)
			if (data[b] >= data[b + 1])
			{
				zim = data[b];
				data[b] = data[b + 1];
				data[b + 1] = zim;
			}
	}
}