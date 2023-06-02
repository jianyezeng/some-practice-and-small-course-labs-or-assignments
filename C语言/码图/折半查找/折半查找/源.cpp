#include<stdio.h>
#pragma warning(disable : 4996)
int main()
{
	int c[100];
	int i = 0;
	int n,zim,b,shuzi;
	int num;
	
	scanf("%d", &n);

	for (i = 0; i <= (n - 1); i++)
		scanf("%d,", &c[i]);
	
	scanf("%d", &shuzi);
	for (i = 0; i < n; i++)
	{
		for (b = 0; b < (n -1- i); b++)
		{
			if (c[i] >= c[i + 1])
			{
				zim = c[i];
				c[i] = c[i + 1];
				c[i + 1] = c[i];
			}
		}
	}
	int numa = 0, numb = (n - 1);
	int x = c[numa], y = c[numb];
	if (shuzi == c[0])
		num = 1;
	else
	{
		if (shuzi == c[n - 1])
			num = n;
		else {
			while (1)
			{
				if (shuzi > (c[(numa + numb) / 2]))
					numa = (numa + numb) / 2;
				else
					if (shuzi < (c[(numa + numb) / 2]))
						numb = (numa + numb) / 2;
					else
					{
						num = (numa + numb) / 2;
						break;
					}
			}
			num = num + 1;
		}
	}
	printf("%d", num);
	
	return 0;
}