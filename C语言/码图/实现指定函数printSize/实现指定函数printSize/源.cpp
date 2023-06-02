#include <stdio.h>
void printSize(int* first, int* last);
int main() {
	int array[257] = { 1,2,3,4 };
	printSize(&array[0], &array[3]);
	return 0;
}
void printSize(int* first, int* last)
{
	if (first == NULL || last == NULL||last-first<=0)
		printf("error");
	int num;
	int size;
	num =int(last - first)+1;
	size = num * 4;
	printf("%d,%d\n", num, size);
}