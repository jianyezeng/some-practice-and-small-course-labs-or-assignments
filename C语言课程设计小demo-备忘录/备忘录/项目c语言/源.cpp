//��Ŀ�����õ�ͷ�ļ�//
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


//����һ���ṹ�����ڴ洢�¼�������ʱ�䡢�����Լ�������Ϣ//
//�ýṹ����������Ϊ�ַ��ͣ����ں���ʹ��InPutbox������Ϣ//
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

//���������������飬������ʱ��ת������//
int inyear[100];
int inmonth[100];
int inday[100];
int inhour[100];
int inminute[100];
int invalue[100];

//����Ϊ�����������˴�ֻ������Ӧ����//
void shuru(int i);//�����ı������û�������洢�¼������ݼ���Ϣ����������txt�ĵ���
int  read();//��txt�ĵ��ж����洢���¼����������¼�����
void shuchu(int n, struct MemoInfox);//�����txt�ĵ��ж��������ݣ����������������ֺͽ���
void countorder(int num, struct MemoInfox);//�Դ�txt�ĵ��е��¼����а���Ҫ��������Ҫ��Խ�ߣ�Խ��ǰ��
void timeorder(int num, struct MemoInfox);//�Դ�txt�ĵ��е��¼����а�ʱ����������ʱ��Խ��Խ��ǰ��
void alarm1();//����1.0
void alarm2();//����2.0
void alarm3();//����3.0
void backout(int num, char* b);//ʵ�ֶ��ض��¼���ɾ������
void checkorder(int num, struct MemoInfox);//�Լ������õ��¼�����һ�ΰ�ʱ������
void checkshuchu(int n, struct MemoInfox);//�Լ������õ��¼��������
void cleanall(int num);//��������¼�
int checkout(int num, char* c);//��txt�ĵ��������¼����м���
void gettotaltime(int num, struct MemoInfox,  long time[]);

IMAGE img;//����һ��ͼ�α�����ȫ�ֱ�����
FILE* infp;//����һ��ָ���ļ���ָ�����infp

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
	initgraph(640, 480, SHOWCONSOLE);//����һ��640*480�Ľ���
	
   //���ñ�����ɫ
	setbkcolor(WHITE);
	cleardevice();//����
	setbkmode(TRANSPARENT);
	settextcolor(BLACK);//����������ɫ
	settextstyle(20, 0, "kaiti");//���������ʽ


	num = read();//���ĵ��е����ݣ������¼�������ֵ��num
	timeorder(num, MemoInfo[100]);//���¼�����
	shuchu(num, MemoInfo[100]);//���¼�����ڽ�����

	
	while (1)//����һ������ѭ������֤���������¼����ѵ���������//
	{
		//atoi�����ɽ��ַ���ת��Ϊ����
		for (n = 0; n < num; n++)
		{
			inyear[n] = atoi (MemoInfo[n].year);
			inmonth[n] = atoi(MemoInfo[n].month);
			inday[n] = atoi(MemoInfo[n].day);
			inhour[n] = atoi(MemoInfo[n].hour);
			inminute[n] = atoi(MemoInfo[n].minute);
			invalue[n] = atoi(MemoInfo[n].value);
		}
		GetLocalTime(&time);//���ϵͳʱ�䣨�����Ե�ʱ�䣩
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
			//��һ���¼����ѣ���������Ϊ�������õ�ʱ�䣬ʮ�ֽ��������¼���Ҫ�̶��޹�//
			if (clock[n].wYear == time.wYear && clock[n].wMonth == time.wMonth && clock[n].wDay == time.wDay && clock[n].wHour == time.wHour && clock[n].wMinute == time.wMinute)
			{
			
				//printf("03");
				alarm1();
			}
			//�ڶ����¼����ѣ���������Ϊ�������õ�ʱ���ǰһ��Сʱ����Ϊ����������Ҫ�̶���5��10֮��//
			if (clock[n].wYear == time.wYear && clock[n].wMonth == time.wMonth && clock[n].wDay == time.wDay && clock[n].wHour - 1 == time.wHour && clock[n].wMinute == time.wMinute && invalue[n] >= 5 && invalue[n] <= 10)
			{
				alarm2();
			}
			//�������¼����ѣ���������Ϊ�������õ�ʱ���ǰһ��Сʱ����Ϊ����������Ҫ�̶ȳ���10//
			if (clock[n].wYear == time.wYear && clock[n].wMonth == time.wMonth && clock[n].wDay == time.wDay && clock[n].wHour - 1 == time.wHour && clock[n].wMinute == time.wMinute && invalue[n] >= 11)
			{
				alarm3();
			}
		}

		
			m = GetMouseMsg();//��ȡ�����Ϣ
			
			if (m.x >= 520 && m.x <= 580 && m.y >= 10 && m.y <= 30)//�ж�����Ƿ�����Ӧ����
			{
				if (m.uMsg == WM_LBUTTONDOWN)//�ж�����Ƿ�����������ǣ���������Ҫ�̶�����
				{
					num = read();
					countorder(num, MemoInfo[100]);
					shuchu(num, MemoInfo[100]);
				}
			}
		
			if (m.x >= 590 && m.x <= 630 && m.y >= 10 && m.y <= 30) // �ж�����Ƿ�����Ӧ����
			{
				if (m.uMsg == WM_LBUTTONDOWN)//�ж�����Ƿ�����������ǣ���������¼�
				{
					num = read();
					shuru(num);
					num = read();
					timeorder(num, MemoInfo[100]);//����¼��������¼��ٽ���һ�ΰ�ʱ������
					shuchu(num, MemoInfo[100]);
				}

			}
			
			if (m.x >= 470 && m.x <= 510 && m.y >= 10 && m.y <= 30)// �ж�����Ƿ�����Ӧ����
			{
				if (m.uMsg == WM_LBUTTONDOWN) // �ж�����Ƿ�����������ǣ�������ʱ������
				{
					num = read();
					timeorder(num, MemoInfo[100]);
					shuchu(num, MemoInfo[100]);
				}
			}
		
			if (m.x >= 420 && m.x <= 460 && m.y >= 10 && m.y <= 30)// �ж�����Ƿ�����Ӧ����
			{
				if (m.uMsg == WM_LBUTTONDOWN)// �ж�����Ƿ�����������ǣ��������
				{
					cleanall(num);
					num = read();
					timeorder(num, MemoInfo[100]);
					shuchu(num, MemoInfo[100]);
				}

			}
			if (m.x >= 320 && m.x <= 360 && m.y >= 10 && m.y <= 30)// �ж�����Ƿ�����Ӧ����
			{
				if (m.uMsg == WM_LBUTTONDOWN)// �ж�����Ƿ�����������ǣ������ض��¼�ɾ��
				{
					//����ؼ��ʺ󣬽������һ�������У���ͨ��backout�������������ݼ�//
					//��������ɸѡ���ض��ؼ��ʶ�Ӧ���¼�������ɾ��//
					InputBox(b, 100, "����������Ҫɾ���¼��Ĺؼ���", "ɾ��", "�ؼ���", 0, 0, false);
					backout(num,  b);
					num = read();
					printf("%d", num);
					timeorder(num, MemoInfo[100]);//��ɾ����ʣ���¼���������//
					shuchu(num, MemoInfo[100]);
				}

			}
			if (m.x >= 370 && m.x <= 410 && m.y >= 10 && m.y <= 30)// �ж�����Ƿ�����Ӧ����
			{
				if (m.uMsg == WM_LBUTTONDOWN)// �ж�����Ƿ�����������ǣ�������������
				{
					//����ؼ��ʺ󣬽������һ�������У���ͨ��checkout�������������ݼ�//
					//��������ɸѡ���ض��ؼ��ʶ�Ӧ���¼������䵥�����//
					InputBox(c, 100, "����������Ҫ�����Ĺؼ���","����", "�ؼ���", 0, 0, false);
					jsnum=checkout(num, c);
					checkorder(jsnum, thing[100]);
					checkshuchu(jsnum,thing[100]);
				}

			}
		}
	}



//ʵ���¼������빦�ܣ�ͨ�������ı�����//
//�û������¼���Ϣ�������䱣����txt�ĵ�//
//��,�����β�i��Ӧtxt�ĵ��е��¼�����//
void shuru(int i)
{
	//��memory.txt�ĵ���ʹ��a+��ԭ�����ļ�����ɾ����//
	//�ļ���дλ�ñ���Ƶ��ļ�ĩβ��������ӣ�Ҳ���Զ�//
	infp = fopen("memory.txt", "a+");
	i++;   
	//�����д���Ϊ����Inputbox�����У����ꡱ��ָ�������ݵ���ʾ������ӡ�Ϊ�ı�����⣬//
	//��2021��ΪĬ�����ݣ�����falseʹ�������ı�����ȡ����ť//
	InputBox(MemoInfo[i].year, 100, "��","���","2021", 0, 0,false);//�Դ���Ϊ����Inputbox�����У����ꡱ��ָ�������ݵ���ʾ������ӡ�Ϊ�ı�����⣬��2021��ΪĬ�����ݣ�����falseʹ�������ı�����ȡ����ť//
	InputBox(MemoInfo[i].month, 100, "��", "���", "1", 0, 0, false);
	InputBox(MemoInfo[i].day, 100, "��", "���", "1", 0, 0, false);
	InputBox(MemoInfo[i].hour, 100, "ʱ", "���", "1", 0, 0, false);
	InputBox(MemoInfo[i].minute, 100, "��", "���", "1", 0, 0, false);
	InputBox(MemoInfo[i].value, 100, "��Ҫ��(������һ�����֣���ֵԽ��Խ��Ҫ)", "���", "1", 0, 0, false);
	InputBox(MemoInfo[i].event, 100, "����", "���", "1", 0, 0, false);
	InputBox(MemoInfo[i].shux, 100, "�¼��Ĺؼ���", "���", "1", 0, 0, false);
   //���û��������Ϣ����txt�ĵ���//
	fprintf(infp, "\n%s,%s,%s,%s,%s,%s,%s,%s", MemoInfo[i].year, MemoInfo[i].month, MemoInfo[i].day,
		MemoInfo[i].hour, MemoInfo[i].minute, MemoInfo[i].value, MemoInfo[i].event,MemoInfo[i].shux);
	fclose(infp);//�ر��ĵ�
}



//��txt�ĵ��ж����洢���¼���Ϣ������ֵΪtxt�ĵ����¼�����
int  read()
{
	int maxn;
	//���ṹ�����㣬����֮ǰ�Խṹ��Ĳ����Ժ�����������в���Ӱ��//
	for (maxn = 0; maxn < 100; maxn++)
	{
		memset(&MemoInfo[maxn], 0, sizeof(MemoInfo[maxn]));
	}
	
	infp = fopen("memory.txt", "a+");//���ĵ�
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
		if (c == EOF)//����ļ��Ƿ񵽴�ĩβ
			break;
		//���ĵ��ж����¼���Ϣ����������ڽṹ���ϣ����ں������//
		fscanf(infp, "%[^,],%[^,],%[^,],%[^,],%[^,],%[^,],%[^,],%s", &MemoInfo[i].year, &MemoInfo[i].month, &MemoInfo[i].day,
			&MemoInfo[i].hour, &MemoInfo[i].minute, &MemoInfo[i].value, &MemoInfo[i].event,&MemoInfo[i].shux);
		i++;//ÿ����һ���¼���i+1�����յõ��¼�����
	}
	fclose(infp);
	return i;//�����¼�����
}

//�����txt�ĵ��ж��������ݣ�������������//
//���֣�������ӣ�ɾ���Ȱ�ť������)�ͽ���//
//�β���nΪ�¼�����//
void shuchu(int n, struct MemoInfox)
{
	cleardevice();//ÿ�������Ҫ����,��Ȼ��ͬ�����ص�
	//����ͼƬbackgroundpicture.jpg,��������//
	loadimage(&img,"./backgroundpicture.jpg", 315, 35);
	putimage(1, 0, &img);

	settextstyle(30, 0, "kaiti");//���������ʽ
	outtextxy(18, 3, "ʱ�������� ����¼");
	settextstyle(20, 0, "kaiti");//���������ʽ
	setfillstyle(BS_SOLID);//���������ʽ��BS_SOLIDΪ��ʵ���
	setfillcolor(RGB(226,231,231));//���������ɫ
	solidrectangle(0,35,240,60);//�����ޱ߿��������
	solidrectangle(240, 35, 320, 60);
	solidrectangle(320, 35, 640, 60);
	setlinecolor(BLACK);//����������ɫ
	line(0, 35, 640, 35);//����ֱ��
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

	setfillcolor(RGB(173,173,173));//���������ɫ
	solidrectangle(315, 3, 365, 35);//�����ޱ߿��������
	solidrectangle(365, 3, 415, 35);
	solidrectangle(415, 3, 465, 35);
	solidrectangle(465, 3, 515, 35);
	solidrectangle(515, 3, 585, 35);
	solidrectangle(585, 3, 635, 35);
	solidrectangle(585, 3, 635, 35);
	outtextxy(520, 10, "��Ҫ��");//�ڽ������������
	outtextxy(590, 10, "���");
	outtextxy(470, 10, "ʱ��");
	outtextxy(420, 10, "���");
	outtextxy(370, 10, "����");
	outtextxy(320, 10, "ɾ��");
	outtextxy(100, 35, "ʱ��");
	outtextxy(350, 35, "���� ");
	outtextxy(575, 35, "�ؼ���");
	outtextxy(250, 35, "��Ҫ�� ");
	setlinecolor(BLACK);//����������ɫ
	line(0, 35, 640, 35);//��ֱ��
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
	setlinecolor(RGB(230, 206, 193));//����������ɫ
	line(240,35,240,60);
	line(570, 35, 570, 60);
	line(320, 35, 320, 60);
	int x;
	if (n == 0) return;//�����¼����������������
	for (x = 0; x < n; x++)
	{
	   //�ڴ˹����н�������ݵ�����������Ϊ����x��һԪһ�κ�������ֹ��ͬ�¼��ص�//
		outtextxy(5, 30* x+65, MemoInfo[x].year);
		outtextxy(65, 30 * x+65, MemoInfo[x].month);
		outtextxy(105, 30 * x+65, MemoInfo[x].day);
		outtextxy(145, 30 * x+65, MemoInfo[x].hour);
		outtextxy(185, 30 * x+65, MemoInfo[x].minute);
		outtextxy(45, 30 * x+65, "��");
		outtextxy(85, 30 * x+65, "�� ");
		outtextxy(125, 30 * x+65, "��");
		outtextxy(165, 30 * x+65, "ʱ");
		outtextxy(205, 30 * x+65, "��");
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




//ʵ�ְ���Ҫ�̶�����//
//�β�numΪ�¼�����//
void countorder(int num, struct MemoInfox)
{
	int x, y;
	char count[100];
	int zim;
	for (x = 0; x < num; x++)
	{
		count[x] = atoi(MemoInfo[x].value);//ʹ��atoi���ַ���Ϊ��ֵ
	}
	//����������Ҫ�ο���ð�������˼·//
	//������İ�ʱ������Ҳ����ˣ�//
	for (y = 0; y< num; y++)
	{
		for (x=0; x <( num - 1-y); x++)
		{
			if (count[x] < count[x + 1])
			{
				//�ṹ����������Ϊ���彻����//
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
//ʵ�ְ�����ʱ������//
//�β�numΪ�¼�����//
void timeorder(int num, struct MemoInfox)
{
	long time[100];
	int x, y=0;
	int zim; 
    long numbea= 0;
	gettotaltime(num, MemoInfo[100], time);//����ʱ�䣨��ʱ�����������ۻ�Ϊ�Է�Ϊ��λ����ֵ�����ڱȽ�
	//��countorder�������ƣ��ο�ð������//
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


//���ַ���ת��Ϊ���֣��������ʱ��//
//(�������ر�ע������timeΪlong�ͣ�//
//������ֵ����),�ú�����Ҫ����ʱ��//
//����ʱ�ıȽ�//
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
//�¼�����1
void alarm1()
{

	// ������
	mciSendString("open background1.mp3 alias mymusic", NULL, 0, NULL);
	// ��������
	mciSendString("play mymusic", NULL, 0, NULL);


	getch();
	// ֹͣ���Ų��ر�����
	mciSendString("stop mymusic", NULL, 0, NULL);
	mciSendString("close mymusic", NULL, 0, NULL);

}
//�¼�����2
void alarm2()
{

	// ������
	mciSendString("open background2.mp3 alias mymusic", NULL, 0, NULL);
	// ��������
	mciSendString("play mymusic", NULL, 0, NULL);
	getch();

	// ֹͣ���Ų��ر�����
	mciSendString("stop mymusic", NULL, 0, NULL);
	mciSendString("close mymusic", NULL, 0, NULL);

	
}
//�¼�����3
void alarm3()
{

	// ������
	mciSendString("open background3.mp3 alias mymusic", NULL, 0, NULL);
	// ��������
	mciSendString("play mymusic", NULL, 0, NULL);

	getch();
	// ֹͣ���Ų��ر�����
	mciSendString("stop mymusic", NULL, 0, NULL);
	mciSendString("close mymusic", NULL, 0, NULL);

}


//����������numΪtxt�ĵ����¼�����
//c[]�д洢֮ǰ����Ĺؼ��ʣ���ʵ��
//�ؼ��ʵıȽϣ��Ӷ�ɸѡ���������
//�¼������������thing��
int checkout(int num,char c[])
{
	int i=0, j;
	int n = 0;
	int longc=0;
	longc = strlen(c);//���ַ����ĳ���(Ϊ�����ؼ��ʱȽ���׼����������Ҳ��ʹ��
	for (j = 0; j < num; j++)
	{
		for (; i < num; i++)
		{
			//�ڹؼ��ʵıȽ��У�ʹ����memcmp����
			//ʹ�øú���ʱ����������ַ���������
			//�Ƚϵ�λ��
			if (memcmp(MemoInfo[i].shux,c,longc)==0)
			{
				thing[n] = MemoInfo[i];
				n++;
			}
		}
	}
	return n;//���ؼ������¼��ĸ���//
}
//�˺�����timeorder����������ͬ����Ϊ��
//����ʹ�ã��ʵ����г������ر�ע�⣬�˴��β�
//Ϊ��������¼�����������txt���¼�����
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

//�˺�����shuchu����������ͬ����Ϊ��//
//����ʹ�ã��ʵ����г������ر�ע�⣬//
//�˴��β�nΪ��������¼�����������//
//txt���¼�����//
void checkshuchu(int n, struct MemoInfox)
{
	cleardevice();//ÿ�������Ҫ����
	loadimage(&img, "./backgroundpicture.jpg", 315, 35);
	putimage(1, 0, &img);
	settextstyle(30, 0, "kaiti");
	outtextxy(18, 3, "ʱ�������� ����¼");
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
	outtextxy(520, 10, "��Ҫ��");
	outtextxy(590, 10, "���");
	outtextxy(470, 10, "ʱ��");
	outtextxy(420, 10, "���");
	outtextxy(370, 10, "����");
	outtextxy(320, 10, "ɾ��");
	outtextxy(100, 35, "ʱ��");
	outtextxy(350, 35, "���� ");
	outtextxy(250, 35, "��Ҫ�� ");
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
		outtextxy(45, 30 * x + 65, "��");
		outtextxy(85, 30 * x + 65, "�� ");
		outtextxy(125, 30 * x + 65, "��");
		outtextxy(165, 30 * x + 65, "ʱ");
		outtextxy(205, 30 * x + 65, "��");
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


//ɾ��������ͨ�����йؼ��ʵıȽϣ�ɾ���ض��¼�  
//�����ض��¼���ɾ��,�Ƚ����¼���Ӧ�ṹ�岿��ɾ��,
//�ٽ������ĵ���գ���ʱ���ṹ�����Դ洢������ɾ��
//���¼���Ϣ���ٽ���д���ĵ��ϣ��ٶ�һ�飬�Ӷ��ﵽ
//ɾ���ض���a����Ŀ��
void backout(int num, char* b)
{


	int i = 0, j;
	int n = 0;
	int longb;
	int z;

	longb = strlen(b);//���ַ����ĳ���(Ϊ�����ؼ��ʱȽ���׼����������Ҳ��ʹ��
	for (i = 0; i < num; i++)
		{
			if (memcmp(MemoInfo[i].shux, b, longb) == 0)
			{
				memset(&MemoInfo[i], 0, sizeof(MemoInfo[i]));//memset�����ɽ��ṹ������
			}
		}
	
	infp = fopen("memory.txt", "w+");//�˴�������w+����ɾ��ԭ�����ļ�������һ�����ļ�
	for (i = 0; i< num; i++)
	{
		n = strlen(MemoInfo[i].year);
		if (n>0)
		{
				fprintf(infp, "\n%s,%s,%s,%s,%s,%s,%s,%s", MemoInfo[i].year, MemoInfo[i].month, MemoInfo[i].day,
					MemoInfo[i].hour, MemoInfo[i].minute, MemoInfo[i].value, MemoInfo[i].event,MemoInfo[i].shux);
		}
	}
	fclose(infp);//�ر��ĵ�
}

//��պ������������¼�ȫ�����//
void cleanall(int num)
{
	int iclean;
	FILE* clear = fopen("memory.txt", "wb+");//wb+��ɾ��ԭ�����ĵ�
	fclose(clear);//�ر��ĵ�
	//�ĵ���ղ��������¼���գ�
	//��Խṹ������������
	for (iclean = 0; iclean < num; iclean++)
	{
		memset(&MemoInfo[iclean], 0, sizeof(MemoInfo[iclean]));
	}
}