#include <stdio.h>
#include<string.h>
#include<graphics.h>
#include<windows.h>
#include<stdlib.h>
#include<time.h>
#include <conio.h>
#include<algorithm>
#include<iostream>
using namespace std;
#pragma comment(lib,"Winmm.lib")	
#pragma warning(disable:4996)
struct MemoInfox
{
	char event[200];
	char year[10];
	char month[10];
	char day[10];
	char hour[10];
	char minute[10];
	char value[10];
	int order;
}MemoInfo[100];
bool camp1(MemoInfox a, MemoInfox b)
{
	if (a.order != b.order)
		return a.order < b.order;//<为升序，>为降序
	else
		return b.order < a.order;
}
bool camp2(MemoInfox a, MemoInfox b)
{
	if (a.order != b.order)
		return a.order < b.order;//<为升序，>为降序
	else
		return b.order < a.order;
}
int inyear[100];
int inmonth[100];
int inday[100];
int inhour[100];
int inminute[100];

void shuru(int i);
int  read();
void shuchu(int n);
void countorder(int num, struct MemoInfox);
void timeorder(int num, struct MemoInfox);
void alarm();


int main()
{
	int a = 0;
	int i;
	int n;
	int num;
	initgraph(640, 480, SHOWCONSOLE);
	//设置背景颜色
	setbkcolor(WHITE);
	cleardevice();//2清屏
	setbkmode(TRANSPARENT);
	settextcolor(BLACK);
	settextstyle(20, 0, "kaiti");


	num = read();

	countorder(num, MemoInfo[100]);
	shuchu(num);
	for (n = 0; n < num; n++)//将字符串转化为数字
	{
		inyear[n] = atoi(MemoInfo[n].year);
		inmonth[n] = atoi(MemoInfo[n].month);
		inday[n] = atoi(MemoInfo[n].day);
		inhour[n] = atoi(MemoInfo[n].hour);
		inminute[n] = atoi(MemoInfo[n].minute);
	}
	SYSTEMTIME time;
	SYSTEMTIME clock[100];
	GetLocalTime(&time);
	for (n = 0; n < num; n++)
	{
		clock[n].wYear = inyear[n];
		clock[n].wMonth = inmonth[n];
		clock[n].wDay = inday[n];
		clock[n].wHour = inhour[n];
		clock[n].wMinute = inminute[n];
	}
	for (n = 0; n < num; n++)
	{
		if (clock[n].wYear == time.wYear && clock[n].wMonth == time.wMonth && clock[n].wDay == time.wDay && clock[n].wHour == time.wHour && clock[n].wMinute == time.wMinute)
		{
			alarm();
		}
	}
	MOUSEMSG m;
	while (a == 0)
	{
		m = GetMouseMsg();
		if (m.x >= 540 && m.x <= 580 && m.y >= 10 && m.y <= 30)//按排序
		{
			if (m.uMsg == WM_LBUTTONDOWN)
			{
				num = read();
				countorder(num, MemoInfo[100]);
				shuchu(num);
			}
		}
		m = GetMouseMsg();
		if (m.x >= 590 && m.x <= 630 && m.y >= 10 && m.y <= 30)
		{
			if (m.uMsg == WM_LBUTTONDOWN)
			{
				num = read();
				printf("%d", num);
				shuru(num);
				num = read();
				countorder(num, MemoInfo[100]);
				shuchu(num);
			}

		}
	}
}
void shuru(int i)
{
	FILE* infp = fopen("memory.txt", "a+");//wb+改成r+
	fseek(infp, 0, SEEK_END);//文件指针移到文件末尾
	i++;
	InputBox(MemoInfo[i].year, 100, "年");
	InputBox(MemoInfo[i].month, 100, "月");
	InputBox(MemoInfo[i].day, 100, "日");
	InputBox(MemoInfo[i].hour, 100, "时");
	InputBox(MemoInfo[i].minute, 100, "分");
	InputBox(MemoInfo[i].value, 100, "重要性(请输入一个数字，数值越大，越重要)");
	InputBox(MemoInfo[i].event, 100, "内容");
	MemoInfo[i].order = i;
	fprintf(infp, "\n%s,%s,%s,%s,%s,%s,%s,%d", &MemoInfo[i].year, &MemoInfo[i].month, &MemoInfo[i].day,
		&MemoInfo[i].hour, &MemoInfo[i].minute, &MemoInfo[i].value, &MemoInfo[i].event, &MemoInfo[i].order);
	fclose(infp);
}
int  read()
{
	FILE* infp = fopen("memory.txt", "a+");
	if (infp == NULL)
	{
		printf("Can't open the file");
		system("pause");
	}
	int i;
	i = 0;
	while (!feof(infp))
	{
		int c = 0;
		if (c == EOF)//检测文件是否到达末尾
			break;
		fscanf(infp, "%[^,],%[^,],%[^,],%[^,],%[^,],%[^,],%s", &MemoInfo[i].year, &MemoInfo[i].month, &MemoInfo[i].day,
			&MemoInfo[i].hour, &MemoInfo[i].minute, &MemoInfo[i].value, &MemoInfo[i].event);
		i++;
	}
	fclose(infp);
	return i;
}
void shuchu(int n)
{
	cleardevice();//每次输出都要清屏
	outtextxy(540, 10, "排序");
	outtextxy(590, 10, "添加");
	outtextxy(490, 10, "清空");
	printf("0");
		for (int x=0;x<n;x++)
		{
			printf("3");
			outtextxy(0, 30 * x, MemoInfo[x].year);
			outtextxy(100, 30 * x, MemoInfo[x].month);
			outtextxy(160, 30 * x, MemoInfo[x].day);
			outtextxy(220, 30 * x, MemoInfo[x].hour);
			outtextxy(300, 30 * x, MemoInfo[x].minute);
			outtextxy(80, 30 * x, "年");
			outtextxy(140, 30 * x, "月 ");
			outtextxy(200, 30 * x, "日");
			outtextxy(260, 30 * x, "时");
			outtextxy(340, 30 * x, "分");
			outtextxy(420, 30 * x, MemoInfo[x].event);
			break;
		}
}



//实现按重要程度排序//
void countorder(int num, struct MemoInfox)
{
	sort(MemoInfo, MemoInfo + 100, camp1);
}
//实现按时间排序//
void timeorder(int num, struct MemoInfox)
{
	sort(MemoInfo, MemoInfo + 100, camp2);
}
//将字符串转化为数字，并求出总时间//
void gettotaltime(int num, struct MemoInfox, long time[])
{
	long year[100];
	long month[100];
	long day[100];
	long hour[100];
	long minute[100];
	for (int x = 1; x < num; x++)
	{
		year[x] = atoi(MemoInfo[x].year);
		month[x] = atoi(MemoInfo[x].month);
		day[x] = atoi(MemoInfo[x].day);
		hour[x] = atoi(MemoInfo[x].hour);
		minute[x] = atoi(MemoInfo[x].minute);
		time[x] = 365 * 24 * 3600 * year[x] + 30 * 24 * 3600 * month[x] + 24 * 3600 * day[x] + 3600 * hour[x] + 60 * minute[x];
	}
}
void alarm()
{
}