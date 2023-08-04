import sys                  #模块sys包含退出游戏的工具

import pygame               #模块pygame包含开发游戏所需的功能

from time import sleep
from scoreboard import Scoreboard
from random import randint
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button

class AlienInvasion:
	"""管理游戏资源和行为的类"""
	def __init__(self):
		pygame.init()       #初始化背景设置

		self.settings =Settings()

		#调用pygame.display.st_mode()来创建一个显示窗口，其中实参（1200，800）为一个元组，指定游戏窗口的尺寸
		#将这个显示窗口赋给属性self.screen
		self.screen = pygame.display.set_mode(
			(self.settings.screen_width,self.settings.screen_height))       
		# self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
		# self.settings.screen_width = self.screen.get_rect().width
		# self.settings.screen_height = self.screen.get_rect().width         
		pygame.display.set_caption("冰墩墩大作战")

		#创建一个用于存储游戏统计信息的实例
		#并创建记分牌
		self.stats = GameStats(self)
		self.s_b = Scoreboard(self)

		self.ship = Ship(self)
		self.bullets = pygame.sprite.Group()
		self.aliens = pygame.sprite.Group()

		self._create_fleet()

		#创建Play按钮
		self.play_button = Button(self,'PLAY')

		#设置背景色
		self.bg_color = (230,230,230)

		#显示等级
		self.s_b.prep_level()



	def run_game(self):
		"""开始游戏的主循环"""
		while True:
			self._check_events()

			if self.stats.game_active:
				self.ship.update()
				self._update_bullets()
				self._update_aliens()

			self._update_screen()



	def _check_events(self):
		"""响应按键和鼠标事件"""

		#监视键盘和鼠标事件
		#函数pygame.event.get() 返回一个列表，包含它在上一次被调用后发生的所有事件
		for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()

				elif event.type == pygame.KEYDOWN:               #每次按键都被注册为一个KEYDOWN事件
					self._check_keydown_events(event)
				elif event.type == pygame.KEYUP:
					self._check_keyup_events(event)
				elif event.type == pygame.MOUSEBUTTONDOWN:
					mouse_pos = pygame.mouse.get_pos()
					self._check_play_button(mouse_pos)

	def _check_keydown_events(self,event):
		"""响应按键"""
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = True
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = True
		elif event.key == pygame.K_UP:
			self.ship.moving_up = True
		elif event.key == pygame.K_DOWN:
			self.ship.moving_down = True

		elif event.key == pygame.K_q:
			sys.exit()

		elif event.key == pygame.K_SPACE:
			self._fire_bullet()

	def _check_keyup_events(self,event):
		"""响应松开"""
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = False
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = False
		elif event.key == pygame.K_UP:
			self.ship.moving_up = False
		elif event.key == pygame.K_DOWN:
			self.ship.moving_down = False



	def _fire_bullet(self):
		"""创建一颗子弹，并将其加入编组bullets中"""
		if len(self.bullets) < self.settings.bullets_allowed:
			self.start_sound_music(self.settings.file_1,0.2)
			new_bullet = Bullet(self)
			self.bullets.add(new_bullet)


	def _update_bullets(self):
		"""更新子弹的位置并删除消失的子弹"""

		#更新子弹的位置
		self.bullets.update()

		#删除消失的子弹
		for bullet in self.bullets.copy():
			if bullet.rect.bottom <= 0:
				self.bullets.remove(bullet)


		self._check_bullet_alien_collisions()

	def _check_bullet_alien_collisions(self):
		"""响应子弹与外星人碰撞"""
		
		#检查是否有子弹击中了外星人
		#如果是，就删除对应的子弹和外星人

		collisions = pygame.sprite.groupcollide(
			self.bullets,self.aliens,True,True)

		if collisions:
			self .start_sound_music(self.settings.file_2,1.0)
			for aliens in collisions.values():
				self.stats.score += self.settings.alien_points * len(aliens) * self.stats.level
			self.s_b.prep_score()
			self.s_b.check_high_score()

		if not self.aliens:
			#升级，删除现有的子弹并新建一群外星人
			self.start_sound_music(self.settings.file_5,1.0)
			self.bullets.empty()
			self.settings.increase_speed( )
			self._create_fleet()

			self.stats.level += 1
			self.s_b.prep_level()



	def _update_screen(self):
		"""更新屏幕上的图像，并切换到新屏幕"""

		#每次循环时都重绘屏幕
		self.screen.fill(self.settings.bg_color)

		self.ship.blitme()

		for bullet in self.bullets.sprites():
			bullet.draw_bullet()

		self.aliens.draw(self.screen)

		#显示得分
		self.s_b.show_score()

		#如果游戏处于非活跃状态，就绘制PLAY按钮
		if not self.stats.game_active:
			self.play_button.draw_button()

		#让最近绘制的屏幕可见
		pygame.display.flip()

	def _create_fleet(self):
		"""创建外星人群。"""
		#创建一个外星人
		alien = Alien(self)
		alien_width, alien_height = alien.rect.size
		available_space_x = self.settings.screen_width - (2 * alien_width)
		number_aliens_x = available_space_x // (2*alien_width)

		#计算屏幕可容纳多少行外星人
		ship_height = self.ship.rect.height
		available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
		number_rows = available_space_y // (2 * alien_height)

		# for row_number in range(number_rows):
		# 	for alien_number in range(number_aliens_x):
		# 		self._create_alien(alien_number,row_number)		
		num = 1
		while num <= self.settings.alien_limits:
			numy = randint(0,number_rows-1)
			numx = randint(0,number_aliens_x-1)
			self._create_alien(numx,numy)
			num += 1


				

	def _create_alien(self,alien_number,row_number): 
		#创建一个外星人并将其加入当前行
		alien = Alien(self)
		alien_width,alien_height = alien.rect.size
		alien.x = alien_width + 2*alien_width * alien_number			
		alien.rect.x = alien.x
		alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
		self.aliens.add(alien)
	
	def _check_fleet_edgs(self):
		"""有外星人到达边缘时采取相应的措施"""
		for alien in self.aliens.sprites():
			if alien.check_edgs():
				self._change_fleet_direction()
				break

	def _change_fleet_direction(self):
		"""将整群外星人下移，并改变他们的方向"""
		for alien in self.aliens.sprites():
			alien.rect.y += self.settings.fleet_drop_speed
		self.settings.fleet_direction *= -1

	def _update_aliens(self):
		"""更新外星人的位置"""
		self._check_fleet_edgs()
		self.aliens.update()

		#检测外星人与飞船之间的碰撞
		if pygame.sprite.spritecollideany(self.ship,self.aliens):
			self._ship_hit()

		#检查是否有外星人到达了屏幕底端
		self._check_aliens_bottom()

	def _ship_hit(self):
		"""响应飞船被外星人撞到"""
		if self.stats.ships_left > 0:

			self.start_sound_music(self.settings.file_4,1.0)
			#将ships_left减1
			self.stats.ships_left -= 1
			self.s_b.prep_ship()

			#清空余下的外星人和子弹
			self.aliens.empty()
			self.bullets.empty()

			#创建一群新的外星人，并将飞船放到屏幕底端的中央
			self._create_fleet()
			self.ship.center_ship()

			#暂停
			sleep(0.5)
		else:
			self.over_music()
			self.start_sound_music(self.settings.file_3,1.0)
			self.stats.game_active = False
			pygame.mouse.set_visible(True)

	def _check_aliens_bottom(self):
		"""检查是否有外星人到达了屏幕底端"""
		screen_rect = self.screen.get_rect()
		for alien in self.aliens.sprites():
			if alien.rect.bottom >= screen_rect.bottom:
				#像飞船被撞到一样处理
				self._ship_hit()
				break

	def _check_play_button(self,mouse_pos):
		"""在玩家单击PLAY按钮时开始新游戏"""
		button_clicked = self.play_button.rect.collidepoint(mouse_pos)
		if button_clicked and not self.stats.game_active:


			#重置游戏设置
			self.settings.initialize_dynamic_settings()

			#播放音乐
			self.start_music()


			#重置游戏统计信息
			self.stats.reset_stats()
			self.stats.game_active = True
			self.s_b.prep_score()
			self.s_b.prep_level()
			self.s_b.prep_ship()

			#清空余下的外星人和子弹
			self.aliens.empty()
			self.bullets.empty()

			#创建一群新的外星人，并让飞船居中
			self._create_fleet()
			self.ship.center_ship()

			#隐藏鼠标光标
			pygame.mouse.set_visible(False)

	def start_music(self):
		"""播放音乐"""
		pygame.mixer.init()						# 初始化
		track_0 = pygame.mixer.music.load(self.settings.file_0)	# 加载音乐文件
		pygame.mixer.music.play(-1)				# 开始播放音乐流

	def over_music(self):
		"""停止播放音乐"""
		pygame.mixer.music.pause()

	def start_sound_music(self,file,soundlevel):
		"""播放音效"""
		pygame.mixer.init()	
		track = pygame.mixer.Sound(file)	# 加载音乐文件
		track.set_volume(soundlevel)
		track.play()				        # 开始播放音乐流



if __name__ == '__main__':
	#创建游戏实例并运行游戏
	ai = AlienInvasion()
	ai.run_game()