#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main() 
{
	int fun(const char* p, int result[]);
	char xuh[14];
	gets_s(xuh);
	int answer[4];
	fun( xuh, answer);
	printf("%d,%d,%d,%d", answer[0], answer[1], answer[2], answer[3]);
	return 0;
}
int fun(const char* p, int result[])
{
	if (*p < '0' || *p>'9' || p == NULL || result == NULL)
		return 0;
	else
	{
		int num;
		num = strlen(p);
		if (num != 13)
			return 0;
		else 
			for (int s = 0; s < 13; s++)
			{
				if (p[s] < '0' || p[s]>'9')
					return 0;
			}
	}
	
		char a[5] = { 0 };
		char b[5] = { 0 };
		char c[5] = { 0 };
		char d[5] = { 0 };
		for (int i = 0; i < 4; i++)
			a[i] = p[i];
		for (int i = 0; i < 2; i++)
			b[i] = p[i+4];
		for (int i = 0; i <4; i++)
			c[i] = p[i + 6];
		for (int i = 0; i < 3; i++)
			d[i] = p[i + 10];
		int x, y, z, zim;
		x = atoi(a); 
		y = atoi(b);
		z = atoi(c);
		zim = atoi(d);
		result[0] = x;
		result[1] = y;
		result[2] = z;
		result[3] = zim;
		return 1;
}