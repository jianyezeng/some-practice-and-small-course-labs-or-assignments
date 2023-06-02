#include <stdio.h>
#pragma warning(disable : 4996)
int main() 
{
	int ReverseArray(int array[], int size);
	int c[6];
	int z=0;
	int b=0;
	for (z = 0; z <5; z++)
		scanf("%d", &c[z]);
	ReverseArray(c,5);
	for (b = 0; b <5; b++)
	{
		printf("%d", c[b]);
	}
	return 0;
}
int ReverseArray(int array[], int size)
{
	int i=1;
	int zim;
	if (size >= 1&&array!=NULL)
	{
		for (i = 0; i <= (size- i-1); i++)
		{
			zim = array[i];
			array[i] = array[size - i-1];
			array[size - i-1 ] = zim;
		}
		return 1;
	}
	else
		return 0;
 }
