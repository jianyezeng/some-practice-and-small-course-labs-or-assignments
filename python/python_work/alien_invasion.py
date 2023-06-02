import sys                  #模块sys包含退出游戏的工具

import pygame               #模块pygame包含开发游戏所需的功能

class AlienInvasion:
	"""管理游戏资源和行为的类"""
	def __init__(self):
		pygame.init()       #初始化背景设置

		#调用pygame.display.st_mode()来创建一个显示窗口，其中实参（1200，800）为一个元组，指定游戏窗口的尺寸
		#将这个显示窗口赋给属性self.screen
		self.screen = pygame.display.set_mode((1200,800))                
		pygame.display.set_caption("Alien Invasion")

		#设置背景色
		self.bg_color = (230,230,230)

	def run_game(self):
		"""开始游戏的主循环"""
		while True:
			#监视键盘和鼠标事件
			#函数pygame.event.get() 返回一个列表，包含它在上一次被调用后发生的所有事件
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()

			#每次循环时都重绘屏幕
			self.screen.fill(self.bg_color)

			#让最近绘制的屏幕可见
			pygame.display.flip()



if __name__ == '__main__':
	#创建游戏实例并运行游戏
	ai = AlienInvasion()
	ai.run_game() 								