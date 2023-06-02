#include<stdio.h>
#include<math.h>
#include<stdlib.h>
#include<time.h>
#pragma warning(disable : 4996)
typedef struct {
	double** mat;
	int row;
	int col;
}Matrix;
void InitialMatrix(Matrix* T, int row, int col);                                          //只分配空间不初始化；
void InitialMatrixZero(Matrix* T, int row, int col);                                     //初始化为0
void InitialMatrixRand(Matrix* T, int row, int col);                                      //初始化为50以内随机正整数
void InputMatrix(Matrix* T);                                                             //键盘输入矩阵
void DestroyMatrix(Matrix* T);                                                            //释放矩阵空间
void PrintfMatrix(Matrix* T);                                                             //矩阵输出
int AddMatrix(Matrix* A, Matrix* B, Matrix* C);                                           //矩阵加
int MinusMatrix(Matrix* A, Matrix* B, Matrix* C);                                         //矩阵减
int MultiMatrix(Matrix* A, Matrix* B, Matrix* C);                                         //矩阵乘法
double MeanMatrix(Matrix* T);                                                             //矩阵元素均值
int SubMatrix(Matrix* T1, Matrix* T2, int BeginRow, int BeginCol, int EndRow, int EndCol);//求T1的子矩阵 T2;

int row, col, row1, col1;                                                                    //定义全局变量，方便在子函数中使用行与列数 

int main()
{
	int i, num;
	Matrix T, T1, T2;
	for (i = 0; i <= 81; i++)
		printf("*");
	printf("\n");
	printf("1:输入一个矩阵，求矩阵均值\n");
	printf("2:产生一个随机矩阵，求矩阵均值\n");
	printf("3:输入两个矩阵，求矩阵和\n");
	printf("4：输入两个矩阵，求矩阵差\n");
	printf("5：输入两个矩阵，求矩阵积\n");
	printf("6：产生两个随机数矩阵，求矩阵和\n");
	printf("7：产生两个随机数矩阵，求矩阵差\n");
	printf("8：产生两个随机数矩阵，求矩阵积\n");
	printf("9：求矩阵的子阵\n");
	printf("0：结束\n");
	for (i = 0; i <= 81; i++)
		printf("*");
	printf("\n");
	printf("请选择功能:\n");
	scanf("%d", &i);
	printf("请输入一个矩阵的行数与列数：\n");
	scanf("%d %d", &row, &col);
	switch (i)
	{
	case 1: InitialMatrix(&T, row, col);
		printf("请输入待计算的矩阵：\n");
		InputMatrix(&T);
		printf("矩阵均值=%.2lf", MeanMatrix(&T));
		DestroyMatrix(&T); break;
	case 2: InitialMatrixRand(&T, row, col);
		printf("矩阵均值=%.2lf", MeanMatrix(&T));  break;
	case 3: InitialMatrix(&T1, row, col);
		InitialMatrix(&T2, row, col);
		printf("请输入待计算的矩阵：\n");
		InputMatrix(&T1);
		InputMatrix(&T2);
		InitialMatrix(&T, row, col);
		printf("结果为：\n");
		AddMatrix(&T1, &T2, &T);
		PrintfMatrix(&T);
		DestroyMatrix(&T1);
		DestroyMatrix(&T2);
		DestroyMatrix(&T); break;
	case 4: InitialMatrix(&T1, row, col);
		InitialMatrix(&T2, row, col);
		printf("请输入待计算的矩阵：\n");
		InputMatrix(&T1);
		InputMatrix(&T2);
		InitialMatrix(&T, row, col);
		MinusMatrix(&T1, &T2, &T);
		printf("结果为：\n");
		PrintfMatrix(&T);
		DestroyMatrix(&T1);
		DestroyMatrix(&T2);
		DestroyMatrix(&T); break;
	case 5: printf("请输入另一个矩阵的行数与列数：\n");
		scanf("%d %d", &row1, &col1);
		InitialMatrix(&T1, row, col);
		InitialMatrix(&T2, row1, col1);
		printf("请输入待计算的矩阵：\n");
		InputMatrix(&T1);
		InputMatrix(&T2);
		InitialMatrix(&T, row, col1);
		printf("结果为：\n");
		num = MultiMatrix(&T1, &T2, &T);
		if (num == 0)
			printf("error");
		else
			PrintfMatrix(&T);
		DestroyMatrix(&T1);
		DestroyMatrix(&T2);
		DestroyMatrix(&T); break;
	case 6: InitialMatrixRand(&T1, row, col);
		InitialMatrixRand(&T2, row, col);
		printf("产生的随机矩阵为：\n");
		PrintfMatrix(&T1);
		PrintfMatrix(&T2);
		InitialMatrix(&T, row, col);
		AddMatrix(&T1, &T2, &T);
		printf("结果为：\n");
		PrintfMatrix(&T);
		DestroyMatrix(&T1);
		DestroyMatrix(&T2);
		DestroyMatrix(&T); break;
	case 7: InitialMatrixRand(&T1, row, col);
		InitialMatrixRand(&T2, row, col);
		InitialMatrix(&T, row, col);
		printf("产生的随机矩阵为：\n");
		PrintfMatrix(&T1);
		PrintfMatrix(&T2);
		MinusMatrix(&T1, &T2, &T);
		printf("结果为：\n");
		PrintfMatrix(&T);
		DestroyMatrix(&T1);
		DestroyMatrix(&T2);
		DestroyMatrix(&T); break;
	case 8: printf("请输入另一个矩阵的行数与列数：\n");
		scanf("%d %d", &row1, &col1);
		InitialMatrixRand(&T1, row, col);
		InitialMatrixRand(&T2, row1, col1);
		printf("产生的随机矩阵为：\n");
		PrintfMatrix(&T1);
		PrintfMatrix(&T2);
		InitialMatrix(&T, row, col1);
		printf("结果为：\n");
		num = MultiMatrix(&T1, &T2, &T);
		if (num == 0)
			printf("error");
		else
			PrintfMatrix(&T);
		DestroyMatrix(&T1);
		DestroyMatrix(&T2);
		DestroyMatrix(&T); break;
	case 9: int BeginRow, BeginCol, EndRow, EndCol;
		InitialMatrix(&T1, row, col);
		printf("请输入待计算的矩阵：\n");
		InputMatrix(&T1);
		printf("请依次输入截取的范围（起始行与列和终止行与列）：\n");
		scanf("%d %d %d %d", &BeginRow, &BeginCol, &EndRow, &EndCol);
		row = EndRow - BeginRow + 1;
		col = EndCol - BeginCol + 1;
		InitialMatrix(&T2, row, col);
		SubMatrix(&T1, &T2, BeginRow, BeginCol, EndRow, EndCol);
		printf("结果为：\n");
		PrintfMatrix(&T2);
		DestroyMatrix(&T1);
		DestroyMatrix(&T2); break;
	case 0: printf("over"); break;
	default: printf("error");
	}
	return 0;
}
void InitialMatrix(Matrix* T, int row, int col)
{
	T->row = row; T->col = col;
	T->mat = (double**)malloc(row * sizeof(double*));
	for (int i = 0; i < row; i++)
		T->mat[i] = (double*)malloc(sizeof(double) * col);
}
void InitialMatrixZero(Matrix* T, int row, int col)
{
	InitialMatrix(T, row, col);
	T->col = col;
	T->row = row;
	T->mat = { 0 };
}
void InitialMatrixRand(Matrix* T, int row, int col)
{
	static int z = 1;
	srand(time(0) * z);
	InitialMatrix(T, row, col);
	for (int i = 0; i < row; i++)
	{
		for (int j = 0; j < col; j++)
			T->mat[i][j] = rand() % 51;
	}
	z++;
}
void InputMatrix(Matrix* T)
{
	for (int i = 0; i < T->row; i++)
	{
		for (int j = 0; j < T->col; j++)
			scanf("%lf", &(T->mat[i][j]));
	}
}
void DestroyMatrix(Matrix* T)
{
	for (int i = 0; i < T->col; i++)
		free(T->mat[i]);
	free(T->mat);
}
void PrintfMatrix(Matrix* T)
{
	for (int i = 0; i < T->row; i++)
	{
		for (int j = 0; j < T->col; j++)
		{
			printf("%.2lf ", T->mat[i][j]);
			if ((j + 1) % T->col == 0)
				printf("\n");
		}
	}
	printf("\n");
}
int AddMatrix(Matrix* A, Matrix* B, Matrix* C)
{
	if (A->row != B->row || A->col != B->col)
		return 0;
	for (int i = 0; i < A->row; i++)
	{
		for (int j = 0; j < A->col; j++)
			C->mat[i][j] = A->mat[i][j] + B->mat[i][j];
	}
	return 1;
}
int MinusMatrix(Matrix* A, Matrix* B, Matrix* C)
{
	if (A->row != B->row || A->col != B->col)
		return 0;
	for (int i = 0; i < A->row; i++)
	{
		for (int j = 0; j < A->col; j++)
			C->mat[i][j] = A->mat[i][j] - B->mat[i][j];
	}
	return 1;
}
int MultiMatrix(Matrix* A, Matrix* B, Matrix* C)
{
	if (A->col != B->row)
		return 0;
	else
	{
		int a = 0;
		for (int i = 0; i < A->row; i++)
			for (int j = 0; j < B->col; j++)
			{
				for (int k = 0; k < A->col; k++)
					a += A->mat[i][k] * B->mat[k][j];
				C->mat[i][j] = a;
				a = 0;
			}
		return 1;
	}
}
double MeanMatrix(Matrix* T)
{
	double sum=0;
	for (int i = 0; i < T->row; i++)
	{
		for (int j = 0; j < T->col; j++)
			sum += T->mat[i][j];
	}
	return sum / (col * row);
}
int SubMatrix(Matrix* T1, Matrix* T2, int BeginRow, int BeginCol, int EndRow, int EndCol)
{
	for (int i = BeginRow - 1, m = 0; i < EndRow; i++, m++)
		for (int j = BeginCol - 1, n = 0; j < EndCol; j++, n++)
			T2->mat[m][n] = T1->mat[i][j];
	return 1;
}

