#include <stdio.h>
#pragma warning(disable : 4996)
struct student
{
	char name[20];
	int sex;
	int birthday;
	float height;
	int scoreC;
	int scoreW;
}stu[100];
int main()
{
	int avarage1,avarage2;
	int max1,max2;
	int min1=0,min2;
	int n, zim;
	int total1=0, total2=0;
	scanf("%d", &n);
	int i,j;
	for (i = 0; i < n; i++)
	{
		scanf("%s", stu[i].name);
		scanf("%d", &stu[i].sex);
		scanf("%d", &stu[i].birthday);
		scanf("%f", &stu[i].height);
		scanf("%d", &stu[i].scoreC);
		scanf("%d", &stu[i].scoreW);
	}
	for (i = 0; i < n; i++)
	{
		total1 += stu[i].scoreC;
		total2 += stu[i].scoreW;
	}
	max1 = stu[0].scoreC;
	min1= stu[0].scoreC;
	avarage1 = total1 / n;
	avarage2 = total2 / n;
	for (j = 0; j < n; j++)
	{
		for (i = 0; i < n - 1 - j; i++)
		{
			if (stu[i].scoreC < stu[i + 1].scoreC)
				max1 = stu[i + 1].scoreC;
		}
	}
	printf("C_average:%d\nC_max:%d\n", avarage1, max1);
	for (i = 0; i < n;i ++)
	{
		
			if (stu[i].scoreC==max1)
				printf("%s %d %d %3.2f %d %d\n", stu[i].name, stu[i].sex, stu[i].birthday, stu[i].height, stu[i].scoreC, stu[i].scoreW);
		
	}
	min1 = stu[0].scoreC;
		for (i = 0; i < n-1; i++)
		{
			if (min1 > stu[i + 1].scoreC)
				min1 = stu[i + 1].scoreC;
		}
	
	printf("C_min:%d\n",min1);
	max2 = stu[0].scoreW;
	
	for (j = 0; j < n; j++)
	{
		for (i = 0; i < n - 1 - j; i++)
		{
			if (stu[i].scoreW < stu[i + 1].scoreW)
				max2 = stu[i + 1].scoreW;
		}
	}
	printf("Calculus_average:%d\nCalculus_max:%d\n", avarage2, max2);
	
		for (i = 0; i < n; i++)
		{
			if (stu[i].scoreW == max2)
				printf("%s %d %d %3.2f %d %d\n", stu[i].name, stu[i].sex, stu[i].birthday, stu[i].height, stu[i].scoreC, stu[i].scoreW);
		}
		min2 = stu[0].scoreW;

		for (i = 0; i < n-1 ; i++)
		{
			if (min2> stu[i + 1].scoreW)
				min2 = stu[i + 1].scoreW;
		}
	
	printf("Calculus_min:%d\n", min2);
	return 0;
}