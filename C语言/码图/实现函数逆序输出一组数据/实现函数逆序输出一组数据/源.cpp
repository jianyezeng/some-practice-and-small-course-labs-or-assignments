#include <stdio.h>
#pragma warning(disable : 4996)
int main()
{
	void isort(int s[], int n);
	int c[1001], i, sizes;
	scanf("%d", &sizes);
	for (i = 0; i < sizes; i++)
		scanf("%d,", &c[i]);
	isort(c, sizes);
	
}
void isort(int s[], int n)
{
	int a = 0;
	int zim;
	for (a = 0; a < (n - a); a++)
	{
		zim = s[a];
		s[a] = s[n - 1 - a];
		s[n - 1 - a] = zim;
	}
	for (a = 0; a < n; a++)
		printf("%d,", s[a]);
} 