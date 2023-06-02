#include <stdio.h>
#include <string.h>
int main()
{
	void count(char* str);
	char c[50];
	gets_s(c);
	count(c);
}
void count(char* str)
{
	int a;
	int numa=0, numb=0, numc=0;
	a = strlen(str);
	for (int x= 0; x <= (a - 1); x++)
	{
		if (str[x]==' ')
			numc=numc+1;
		else
			if (str[x] <= '9' && str[x] >= '0')
				numb=numb+1;
			else
				if (str[x] >= 'a' && str[x] <= 'z' || str[x] >= 'A' && str[x] <= 'Z')
					numa=numa+1;
	}
	printf("%d,%d,%d", numa, numb, numc);
}