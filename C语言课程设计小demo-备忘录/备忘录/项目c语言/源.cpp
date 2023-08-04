//项目所引用的头文件//
#include <stdio.h>
#include<string.h>
#include<graphics.h>
#include <mmsystem.h>
#include<windows.h>
#include<stdlib.h>
#include<time.h>
#include <conio.h>
#include<algorithm>
#include<iostream>
using namespace std;
#pragma comment(lib,"Winmm.lib")	
#pragma warning(disable:4996)


//创建一个结构体用于存储事件的提醒时间、内容以及其他信息//
//该结构体包含数组均为字符型，便于后续使用InPutbox输入信息//
struct MemoInfox
{
	char event[200];
	char year[10];
	char month[10];
	char day[10];
	char hour[10];
	char minute[10];
	char value[10];
	char shux[10];
}MemoInfo[100];
struct MemoInfox text;
struct MemoInfox thing[100];

//定义以下整型数组，将用于时间转换部分//
int inyear[100];
int inmonth[100];
int inday[100];
int inhour[100];
int inminute[100];
int invalue[100];

//以下为函数声明，此处只给出对应功能//
void shuru(int i);//弹出文本框，让用户输入需存储事件的内容及信息，并保存在txt文档中
int  read();//从txt文档中读出存储的事件，并返回事件个数
void shuchu(int n, struct MemoInfox);//输出从txt文档中读到的内容，及其他功能性文字和界面
void countorder(int num, struct MemoInfox);//对从txt文档中的事件进行按重要性排序（重要性越高，越靠前）
void timeorder(int num, struct MemoInfox);//对从txt文档中的事件进行按时间排序（提醒时间越晚，越靠前）
void alarm1();//提醒1.0
void alarm2();//提醒2.0
void alarm3();//提醒3.0
void backout(int num, char* b);//实现对特定事件的删除功能
void checkorder(int num, struct MemoInfox);//对检索所得的事件进行一次按时间排序
void checkshuchu(int n, struct MemoInfox);//对检索所得的事件进行输出
void cleanall(int num);//清空所有事件
int checkout(int num, char* c);//对txt文档中所存事件进行检索
void gettotaltime(int num, struct MemoInfox,  long time[]);

IMAGE img;//定义一个图形变量（全局变量）
FILE* infp;//定义一个指向文件的指针变量infp

int main()
{
	int jsnum;
	int backnum;
	char c[100];
	char b[100];
	int a = 0;
	int i, n, zim, num;

	MOUSEMSG m;

	SYSTEMTIME time;
	SYSTEMTIME clock[100];
	initgraph(640, 480, SHOWCONSOLE);//创建一个640*480的界面
	
   //设置背景颜色
	setbkcolor(WHITE);
	cleardevice();//清屏
	setbkmode(TRANSPARENT);
	settextcolor(BLACK);//设置字体颜色
	settextstyle(20, 0, "kaiti");//设置字体格式


	num = read();//读文档中的内容，并把事件个数赋值给num
	timeorder(num, MemoInfo[100]);//将事件排序
	shuchu(num, MemoInfo[100]);//将事件输出在界面上

	
	while (1)//设置一个无限循环，保证鼠标操作及事件提醒的正常进行//
	{
		//atoi函数可将字符串转化为数字
		for (n = 0; n < num; n++)
		{
			inyear[n] = atoi (MemoInfo[n].year);
			inmonth[n] = atoi(MemoInfo[n].month);
			inday[n] = atoi(MemoInfo[n].day);
			inhour[n] = atoi(MemoInfo[n].hour);
			inminute[n] = atoi(MemoInfo[n].minute);
			invalue[n] = atoi(MemoInfo[n].value);
		}
		GetLocalTime(&time);//获得系统时间（即电脑的时间）
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
			//第一种事件提醒，触发条件为到达设置的时间，十分紧急，与事件重要程度无关//
			if (clock[n].wYear == time.wYear && clock[n].wMonth == time.wMonth && clock[n].wDay == time.wDay && clock[n].wHour == time.wHour && clock[n].wMinute == time.wMinute)
			{
			
				//printf("03");
				alarm1();
			}
			//第二种事件提醒，触发条件为到达设置的时间的前一个小时，较为紧急，且重要程度在5与10之间//
			if (clock[n].wYear == time.wYear && clock[n].wMonth == time.wMonth && clock[n].wDay == time.wDay && clock[n].wHour - 1 == time.wHour && clock[n].wMinute == time.wMinute && invalue[n] >= 5 && invalue[n] <= 10)
			{
				alarm2();
			}
			//第三种事件提醒，触发条件为到达设置的时间的前一个小时，较为紧急，且重要程度超过10//
			if (clock[n].wYear == time.wYear && clock[n].wMonth == time.wMonth && clock[n].wDay == time.wDay && clock[n].wHour - 1 == time.wHour && clock[n].wMinute == time.wMinute && invalue[n] >= 11)
			{
				alarm3();
			}
		}

		
			m = GetMouseMsg();//获取鼠标信息
			
			if (m.x >= 520 && m.x <= 580 && m.y >= 10 && m.y <= 30)//判断鼠标是否在相应区域
			{
				if (m.uMsg == WM_LBUTTONDOWN)//判断鼠标是否按下左键，若是，触发按重要程度排序
				{
					num = read();
					countorder(num, MemoInfo[100]);
					shuchu(num, MemoInfo[100]);
				}
			}
		
			if (m.x >= 590 && m.x <= 630 && m.y >= 10 && m.y <= 30) // 判断鼠标是否在相应区域
			{
				if (m.uMsg == WM_LBUTTONDOWN)//判断鼠标是否按下左键，若是，触发添加事件
				{
					num = read();
					shuru(num);
					num = read();
					timeorder(num, MemoInfo[100]);//添加事件后将所有事件再进行一次按时间排序
					shuchu(num, MemoInfo[100]);
				}

			}
			
			if (m.x >= 470 && m.x <= 510 && m.y >= 10 && m.y <= 30)// 判断鼠标是否在相应区域
			{
				if (m.uMsg == WM_LBUTTONDOWN) // 判断鼠标是否按下左键，若是，触发按时间排序
				{
					num = read();
					timeorder(num, MemoInfo[100]);
					shuchu(num, MemoInfo[100]);
				}
			}
		
			if (m.x >= 420 && m.x <= 460 && m.y >= 10 && m.y <= 30)// 判断鼠标是否在相应区域
			{
				if (m.uMsg == WM_LBUTTONDOWN)// 判断鼠标是否按下左键，若是，触发清空
				{
					cleanall(num);
					num = read();
					timeorder(num, MemoInfo[100]);
					shuchu(num, MemoInfo[100]);
				}

			}
			if (m.x >= 320 && m.x <= 360 && m.y >= 10 && m.y <= 30)// 判断鼠标是否在相应区域
			{
				if (m.uMsg == WM_LBUTTONDOWN)// 判断鼠标是否按下左键，若是，触发特定事件删除
				{
					//输入关键词后，将其存在一个数组中，并通过backout函数（具体内容见//
					//主函数后）筛选出特定关键词对应的事件，将其删除//
					InputBox(b, 100, "请输入您需要删除事件的关键词", "删除", "关键词", 0, 0, false);
					backout(num,  b);
					num = read();
					printf("%d", num);
					timeorder(num, MemoInfo[100]);//将删除后剩余事件进行排序//
					shuchu(num, MemoInfo[100]);
				}

			}
			if (m.x >= 370 && m.x <= 410 && m.y >= 10 && m.y <= 30)// 判断鼠标是否在相应区域
			{
				if (m.uMsg == WM_LBUTTONDOWN)// 判断鼠标是否按下左键，若是，触发检索功能
				{
					//输入关键词后，将其存在一个数组中，并通过checkout函数（具体内容见//
					//主函数后）筛选出特定关键词对应的事件，将其单独输出//
					InputBox(c, 100, "请输入您需要检索的关键词","检索", "关键词", 0, 0, false);
					jsnum=checkout(num, c);
					checkorder(jsnum, thing[100]);
					checkshuchu(jsnum,thing[100]);
				}

			}
		}
	}



//实现事件的输入功能，通过弹出文本框，让//
//用户输入事件信息，并将其保存在txt文档//
//中,其中形参i对应txt文档中的事件个数//
void shuru(int i)
{
	//打开memory.txt文档（使用a+，原来的文件不被删除，//
	//文件读写位置标记移到文件末尾，可以添加，也可以读//
	infp = fopen("memory.txt", "a+");
	i++;   
	//以下行代码为例，Inputbox函数中，“年”是指输入内容的提示，“添加”为文本框标题，//
	//“2021”为默认内容，最后的false使弹出的文本框有取消按钮//
	InputBox(MemoInfo[i].year, 100, "年","添加","2021", 0, 0,false);//以此行为例，Inputbox函数中，“年”是指输入内容的提示，“添加”为文本框标题，“2021”为默认内容，最后的false使弹出的文本框有取消按钮//
	InputBox(MemoInfo[i].month, 100, "月", "添加", "1", 0, 0, false);
	InputBox(MemoInfo[i].day, 100, "日", "添加", "1", 0, 0, false);
	InputBox(MemoInfo[i].hour, 100, "时", "添加", "1", 0, 0, false);
	InputBox(MemoInfo[i].minute, 100, "分", "添加", "1", 0, 0, false);
	InputBox(MemoInfo[i].value, 100, "重要性(请输入一个数字，数值越大，越重要)", "添加", "1", 0, 0, false);
	InputBox(MemoInfo[i].event, 100, "内容", "添加", "1", 0, 0, false);
	InputBox(MemoInfo[i].shux, 100, "事件的关键词", "添加", "1", 0, 0, false);
   //将用户输入的信息存在txt文档中//
	fprintf(infp, "\n%s,%s,%s,%s,%s,%s,%s,%s", MemoInfo[i].year, MemoInfo[i].month, MemoInfo[i].day,
		MemoInfo[i].hour, MemoInfo[i].minute, MemoInfo[i].value, MemoInfo[i].event,MemoInfo[i].shux);
	fclose(infp);//关闭文档
}



//从txt文档中读出存储的事件信息，返回值为txt文档中事件个数
int  read()
{
	int maxn;
	//将结构体清零，避免之前对结构体的操作对后续程序的运行产生影响//
	for (maxn = 0; maxn < 100; maxn++)
	{
		memset(&MemoInfo[maxn], 0, sizeof(MemoInfo[maxn]));
	}
	
	infp = fopen("memory.txt", "a+");//打开文档
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
		c = fgetc(infp);
		if (c == EOF)//检测文件是否到达末尾
			break;
		//从文档中读出事件信息，并将其存在结构体上，便于后续输出//
		fscanf(infp, "%[^,],%[^,],%[^,],%[^,],%[^,],%[^,],%[^,],%s", &MemoInfo[i].year, &MemoInfo[i].month, &MemoInfo[i].day,
			&MemoInfo[i].hour, &MemoInfo[i].minute, &MemoInfo[i].value, &MemoInfo[i].event,&MemoInfo[i].shux);
		i++;//每读出一个事件，i+1，最终得到事件个数
	}
	fclose(infp);
	return i;//返回事件个数
}

//输出从txt文档中读到的内容，及其他功能性//
//文字（例如添加，删除等按钮的文字)和界面//
//形参中n为事件个数//
void shuchu(int n, struct MemoInfox)
{
	cleardevice();//每次输出都要清屏,不然不同内容重叠
	//插入图片backgroundpicture.jpg,美化界面//
	loadimage(&img,"./backgroundpicture.jpg", 315, 35);
	putimage(1, 0, &img);

	settextstyle(30, 0, "kaiti");//设置字体格式
	outtextxy(18, 3, "时间管理软件 备忘录");
	settextstyle(20, 0, "kaiti");//设置字体格式
	setfillstyle(BS_SOLID);//设置填充样式，BS_SOLID为固实填充
	setfillcolor(RGB(226,231,231));//设置填充颜色
	solidrectangle(0,35,240,60);//画出无边框的填充矩形
	solidrectangle(240, 35, 320, 60);
	solidrectangle(320, 35, 640, 60);
	setlinecolor(BLACK);//设置字体颜色
	line(0, 35, 640, 35);//画出直线
	line(0, 35, 0, 60);
	line(0, 0, 0, 35);
	line(315, 3, 315, 35);
	line(365, 3, 365, 35);
	line(415, 3, 415, 35);
	line(465, 3, 465, 35);
	line(515, 3, 515, 35);
	line(585, 3, 585, 35);
	line(635, 3, 635, 35);
	line(639, 35, 639, 60);

	setfillcolor(RGB(173,173,173));//设置填充颜色
	solidrectangle(315, 3, 365, 35);//画出无边框的填充矩形
	solidrectangle(365, 3, 415, 35);
	solidrectangle(415, 3, 465, 35);
	solidrectangle(465, 3, 515, 35);
	solidrectangle(515, 3, 585, 35);
	solidrectangle(585, 3, 635, 35);
	solidrectangle(585, 3, 635, 35);
	outtextxy(520, 10, "重要性");//在界面上输出文字
	outtextxy(590, 10, "添加");
	outtextxy(470, 10, "时间");
	outtextxy(420, 10, "清空");
	outtextxy(370, 10, "检索");
	outtextxy(320, 10, "删除");
	outtextxy(100, 35, "时间");
	outtextxy(350, 35, "内容 ");
	outtextxy(575, 35, "关键词");
	outtextxy(250, 35, "重要性 ");
	setlinecolor(BLACK);//设置字体颜色
	line(0, 35, 640, 35);//画直线
	line(0, 35, 0, 60);
	line(0, 0, 0, 35);
	line(315, 3, 315, 32);
	line(365, 3, 365, 32);
	line(415, 3, 415, 32);
	line(465, 3, 465, 32);
	line(515, 3, 515, 32);
	line(585, 3, 585, 32);
	line(635, 3, 635, 32);
	line(639, 35, 639, 60);
	setlinecolor(RGB(230, 206, 193));//设置线条颜色
	line(240,35,240,60);
	line(570, 35, 570, 60);
	line(320, 35, 320, 60);
	int x;
	if (n == 0) return;//若无事件，不输出以下内容
	for (x = 0; x < n; x++)
	{
	   //在此过程中将输出内容的纵坐标设置为关于x的一元一次函数，防止不同事件重叠//
		outtextxy(5, 30* x+65, MemoInfo[x].year);
		outtextxy(65, 30 * x+65, MemoInfo[x].month);
		outtextxy(105, 30 * x+65, MemoInfo[x].day);
		outtextxy(145, 30 * x+65, MemoInfo[x].hour);
		outtextxy(185, 30 * x+65, MemoInfo[x].minute);
		outtextxy(45, 30 * x+65, "年");
		outtextxy(85, 30 * x+65, "月 ");
		outtextxy(125, 30 * x+65, "日");
		outtextxy(165, 30 * x+65, "时");
		outtextxy(205, 30 * x+65, "分");
		outtextxy(270, 30 * x + 65, MemoInfo[x].value);
		outtextxy(580, 30 * x + 65, MemoInfo[x].shux);
		outtextxy(330, 30 * x+65, MemoInfo[x].event);
		setlinecolor(RGB(230,206,193));
		line(240, 60 + 30 * x, 240, 90 + 30 * x);
		line(320, 60 + 30 * x, 320, 90 + 30 * x);
		line(570, 60 + 30 * x, 570, 90 + 30 * x);
		setlinecolor(BLACK);
		line(0,60 + 30 * x, 640, 60 + 30 * x);
		line(0, 90 + 30 * x, 640, 90 + 30 * x);
		line(0, 60 + 30 * x, 0, 90 + 30 * x);
		line(639, 60 + 30 * x, 639, 90 + 30 * x);
	}
}




//实现按重要程度排序//
//形参num为事件个数//
void countorder(int num, struct MemoInfox)
{
	int x, y;
	char count[100];
	int zim;
	for (x = 0; x < num; x++)
	{
		count[x] = atoi(MemoInfo[x].value);//使用atoi将字符变为数值
	}
	//关于排序，主要参考了冒泡排序的思路//
	//（后面的按时间排序也是如此）//
	for (y = 0; y< num; y++)
	{
		for (x=0; x <( num - 1-y); x++)
		{
			if (count[x] < count[x + 1])
			{
				//结构体是允许作为整体交换的//
				zim = count[x];
				count[x] = count[x + 1];
				count[x + 1] = zim;
				text = MemoInfo[x];
				MemoInfo[x] = MemoInfo[x + 1];
				MemoInfo[x + 1] = text;
			}
		}
	}
}
//实现按提醒时间排序//
//形参num为事件个数//
void timeorder(int num, struct MemoInfox)
{
	long time[100];
	int x, y=0;
	int zim; 
    long numbea= 0;
	gettotaltime(num, MemoInfo[100], time);//求总时间（将时间的相关数据折换为以分为单位的数值，便于比较
	//与countorder函数类似，参考冒泡排序//
	for (x =0; x < num; x++)
	{
		for (y=0; y < (num-1-x); y++)
		{
			if (time[y] < time[y + 1])
			{
				numbea = time[y];
				time[y] = time[y + 1];
				time[y + 1] = numbea;
				text = MemoInfo[y];
				MemoInfo[y] = MemoInfo[y + 1];
				MemoInfo[y + 1] = text;
			}
		}
	}
}


//将字符串转化为数字，并求出总时间//
//(另外需特别注意数组time为long型，//
//避免数值过大),该函数主要用于时间//
//排序时的比较//
void gettotaltime(int num, struct MemoInfox, long time[])
{
	long year[100];
	long month[100];
	long day[100];
	long hour[100];
	long minute[100];
	for (int x = 0; x < num; x++)
	{
		year[x] = atol(MemoInfo[x].year);
		month[x] = atol(MemoInfo[x].month);
		day[x] = atol(MemoInfo[x].day);
		hour[x] = atol(MemoInfo[x].hour);
		minute[x] = atol(MemoInfo[x].minute);
		time[x] = 365 * 24 * 60 * year[x] + 30 * 24 * 60 * month[x] + 24 * 60 * day[x] + 60 * hour[x] +  minute[x];
	}
}
//事件提醒1
void alarm1()
{

	// 打开音乐
	mciSendString("open background1.mp3 alias mymusic", NULL, 0, NULL);
	// 播放音乐
	mciSendString("play mymusic", NULL, 0, NULL);


	getch();
	// 停止播放并关闭音乐
	mciSendString("stop mymusic", NULL, 0, NULL);
	mciSendString("close mymusic", NULL, 0, NULL);

}
//事件提醒2
void alarm2()
{

	// 打开音乐
	mciSendString("open background2.mp3 alias mymusic", NULL, 0, NULL);
	// 播放音乐
	mciSendString("play mymusic", NULL, 0, NULL);
	getch();

	// 停止播放并关闭音乐
	mciSendString("stop mymusic", NULL, 0, NULL);
	mciSendString("close mymusic", NULL, 0, NULL);

	
}
//事件提醒3
void alarm3()
{

	// 打开音乐
	mciSendString("open background3.mp3 alias mymusic", NULL, 0, NULL);
	// 播放音乐
	mciSendString("play mymusic", NULL, 0, NULL);

	getch();
	// 停止播放并关闭音乐
	mciSendString("stop mymusic", NULL, 0, NULL);
	mciSendString("close mymusic", NULL, 0, NULL);

}


//检索函数，num为txt文档中事件个数
//c[]中存储之前输入的关键词，可实现
//关键词的比较，从而筛选出需检索的
//事件，并将其存在thing中
int checkout(int num,char c[])
{
	int i=0, j;
	int n = 0;
	int longc=0;
	longc = strlen(c);//求字符串的长度(为后续关键词比较做准备），汉字也可使用
	for (j = 0; j < num; j++)
	{
		for (; i < num; i++)
		{
			//在关键词的比较中，使用了memcmp函数
			//使用该函数时需给出两个字符串，及需
			//比较的位数
			if (memcmp(MemoInfo[i].shux,c,longc)==0)
			{
				thing[n] = MemoInfo[i];
				n++;
			}
		}
	}
	return n;//返回检索出事件的个数//
}
//此函数与timeorder函数基本相同，但为了
//方便使用，故单独列出，需特别注意，此处形参
//为需检索的事件个数，而非txt中事件个数
void checkorder(int num, struct MemoInfox)
{
	long time[100];
	int x, y = 0;
	int zim;
	long numbea = 0;
	gettotaltime(num, thing[100], time);
	for (x = 0; x < num; x++)
	{
		for (y = 0; y < (num - 1 - x); y++)
		{
			if (time[y] < time[y + 1])
			{
				numbea = time[y];
				time[y] = time[y + 1];
				time[y + 1] = numbea;
				text =thing[y];
				thing[y] = thing[y + 1];
				thing[y + 1] = text;
			}
		}
	}
}

//此函数与shuchu函数基本相同，但为了//
//方便使用，故单独列出，需特别注意，//
//此处形参n为需检索的事件个数，而非//
//txt中事件个数//
void checkshuchu(int n, struct MemoInfox)
{
	cleardevice();//每次输出都要清屏
	loadimage(&img, "./backgroundpicture.jpg", 315, 35);
	putimage(1, 0, &img);
	settextstyle(30, 0, "kaiti");
	outtextxy(18, 3, "时间管理软件 备忘录");
	settextstyle(20, 0, "kaiti");
	setfillstyle(BS_SOLID);
	setfillcolor(RGB(226, 231, 231));
	solidrectangle(0, 35, 240, 60);
	setfillcolor(RGB(226, 231, 231));
	solidrectangle(240, 35, 320, 60);
	setfillcolor(RGB(226, 231, 231));
	solidrectangle(320, 35, 640, 60);

	setlinecolor(BLACK);
	line(0, 35, 640, 35);
	line(0, 35, 0, 60);
	line(0, 0, 0, 35);
	line(315, 3, 315, 35);
	line(365, 3, 365, 35);
	line(415, 3, 415, 35);
	line(465, 3, 465, 35);
	line(515, 3, 515, 35);
	line(585, 3, 585, 35);
	line(635, 3, 635, 35);
	line(639, 35, 639, 60);
	setfillcolor(RGB(173, 173, 173));
	solidrectangle(315, 3, 365, 35);
	solidrectangle(365, 3, 415, 35);
	solidrectangle(415, 3, 465, 35);
	solidrectangle(465, 3, 515, 35);
	solidrectangle(515, 3, 585, 35);
	solidrectangle(585, 3, 635, 35);
	solidrectangle(585, 3, 635, 35);
	outtextxy(520, 10, "重要性");
	outtextxy(590, 10, "添加");
	outtextxy(470, 10, "时间");
	outtextxy(420, 10, "清空");
	outtextxy(370, 10, "检索");
	outtextxy(320, 10, "删除");
	outtextxy(100, 35, "时间");
	outtextxy(350, 35, "内容 ");
	outtextxy(250, 35, "重要性 ");
	setlinecolor(BLACK);
	line(0, 35, 640, 35);
	line(0, 35, 0, 60);
	line(0, 0, 0, 35);
	line(315, 3, 315, 32);
	line(365, 3, 365, 32);
	line(415, 3, 415, 32);
	line(465, 3, 465, 32);
	line(515, 3, 515, 32);
	line(585, 3, 585, 32);
	line(635, 3, 635, 32);
	line(639, 35, 639, 60);
	setlinecolor(RGB(230, 206, 193));
	line(240, 35, 240, 60);
	line(320, 35, 320, 60);
	int x;
	if (n == 0) return;
	for (x = 0; x < n; x++)
	{
		outtextxy(5, 30 * x + 65, thing[x].year);
		outtextxy(65, 30 * x + 65, thing[x].month);
		outtextxy(105, 30 * x + 65, thing[x].day);
		outtextxy(145, 30 * x + 65, thing[x].hour);
		outtextxy(185, 30 * x + 65, thing[x].minute);
		outtextxy(45, 30 * x + 65, "年");
		outtextxy(85, 30 * x + 65, "月 ");
		outtextxy(125, 30 * x + 65, "日");
		outtextxy(165, 30 * x + 65, "时");
		outtextxy(205, 30 * x + 65, "分");
		outtextxy(270, 30 * x + 65, thing[x].value);
		outtextxy(330, 30 * x + 65, thing[x].event);
		setlinecolor(RGB(230, 206, 193));
		line(240, 60 + 30 * x, 240, 90 + 30 * x);
		line(320, 60 + 30 * x, 320, 90 + 30 * x);
		setlinecolor(BLACK);
		line(0, 60 + 30 * x, 640, 60 + 30 * x);
		line(0, 90 + 30 * x, 640, 90 + 30 * x);
		line(0, 60 + 30 * x, 0, 90 + 30 * x);
		line(639, 60 + 30 * x, 639, 90 + 30 * x);
	}
}


//删除函数，通过进行关键词的比较，删除特定事件  
//对于特定事件的删除,先将该事件对应结构体部分删除,
//再将整个文档清空，此时，结构体中仍存储着无需删除
//的事件信息，再将其写再文档上，再读一遍，从而达到
//删除特定事a件的目的
void backout(int num, char* b)
{


	int i = 0, j;
	int n = 0;
	int longb;
	int z;

	longb = strlen(b);//求字符串的长度(为后续关键词比较做准备），汉字也可使用
	for (i = 0; i < num; i++)
		{
			if (memcmp(MemoInfo[i].shux, b, longb) == 0)
			{
				memset(&MemoInfo[i], 0, sizeof(MemoInfo[i]));//memset函数可将结构体清零
			}
		}
	
	infp = fopen("memory.txt", "w+");//此处采用了w+，会删除原来的文件，建立一个新文件
	for (i = 0; i< num; i++)
	{
		n = strlen(MemoInfo[i].year);
		if (n>0)
		{
				fprintf(infp, "\n%s,%s,%s,%s,%s,%s,%s,%s", MemoInfo[i].year, MemoInfo[i].month, MemoInfo[i].day,
					MemoInfo[i].hour, MemoInfo[i].minute, MemoInfo[i].value, MemoInfo[i].event,MemoInfo[i].shux);
		}
	}
	fclose(infp);//关闭文档
}

//清空函数，将所有事件全部清空//
void cleanall(int num)
{
	int iclean;
	FILE* clear = fopen("memory.txt", "wb+");//wb+可删除原来的文档
	fclose(clear);//关闭文档
	//文档清空并不代表事件清空，
	//需对结构体进行清零操作
	for (iclean = 0; iclean < num; iclean++)
	{
		memset(&MemoInfo[iclean], 0, sizeof(MemoInfo[iclean]));
	}
}