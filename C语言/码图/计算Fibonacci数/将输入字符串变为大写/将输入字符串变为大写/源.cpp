#include <stdio.h>
int main()
{
	char c[27];
	int len = 1;
	c[len] = getchar();
	for (len=1; c[len] >= 65 && c[len] <= 90;len++)
  
	printf("%c", c[len]);
	return 0;
}