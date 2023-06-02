#include <stdio.h>
#pragma warning(disable : 4996)
int main()
{
	int lif(int x);
	int find(int n);
	int shuzi,d;
	scanf("%d", &shuzi);
	d=find(shuzi);
	printf("%d", d);
	return 0;
}
int find(int n)
{
	int lif(int x);
	int i = 100;
	int num = 0;
	int a, b, c;
	if (n < 100 || n>999)
		return 0;
	else
	{
		for (i = 100; i <= n; i++)
		{
			a = (int)(i / 100);
			c = i % 10;
			b = (i - 100 * a - c) / 10;
			if (i == lif(a) + lif(b) + lif(c))
				num = num + 1;
		}
			return (num);
	}
}
int lif(int x)
{
	int y;
	y = x * x * x;
	return (y);
}