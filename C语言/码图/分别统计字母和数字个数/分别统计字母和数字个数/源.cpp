#include <stdio.h>
#include <string>
int main()
{
	int numa=0, numb=0;
	char i;
	while(1)
	{
		i = getchar();
		if (i != '\n')
		{
			if (i >= '0' && i <= '9')
				numb++;
			if (i >= 'a' && i <= 'z' || i >= 'A' && i <= 'Z')
				numa++;
		}
		else
			break;
	}
	printf("letters:%d,digits:%d", numa, numb);
	return 0;
}