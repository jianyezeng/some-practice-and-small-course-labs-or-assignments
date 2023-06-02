#include<stdio.h>
#pragma warning(disable : 4996) 
void swap(int* array, int n)
{
	int i = 0;
	int zim;

	if (array != NULL && n >= 1)
	{
		zim = array[0];
		array[0] = array[n - 1];
		array[n - 1] = zim;
	}
	else
	{
		printf("error");
	}
}
int main()
{
	
void swap(int* array, int n);
	
 
	int c[5],a;
	for (a = 0; a < 5; a++)
		scanf("%d", &c[a]);

	swap(c, 5);
	return 0;
}
