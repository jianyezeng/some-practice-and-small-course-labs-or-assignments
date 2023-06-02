class Settings:
	"""存储游戏【外星人入侵】中所有设置的类"""

	def __init__(self):
		"""初始化游戏的静态设置"""

		#屏幕设置
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230,230,230)

		#音乐设置
		self.file_0 = r'C:\\Users\\zjy\\Desktop\\alien_invasion\\music\\bgmusic.mp3'
		self.file_1 = r'C:\\Users\\zjy\\Desktop\\alien_invasion\\music\\bullet_music.mp3'
		self.file_2 = r'C:\\Users\\zjy\\Desktop\\alien_invasion\\music\\bit_music.mp3'
		self.file_3 = r'C:\\Users\\zjy\\Desktop\\alien_invasion\\music\\finish_failure.mp3'
		self.file_4 = r'C:\\Users\\zjy\\Desktop\\alien_invasion\\music\\failure.mp3'
		self.file_5 = r'C:\\Users\\zjy\\Desktop\\alien_invasion\\music\\success.mp3'


		#飞船设置
		self.ship_speed = 0.8
		self.ship_limit = 2

		#子弹设置
		self.bullet_speed = 1.0
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (60,60,60)

		self.bullets_allowed = 3

		#外星人设置
		self.alien_speed = 0.2
		self.fleet_drop_speed = 10
		#self.fleet_direction为1表示向右移，为-1表示向左移
		self.fleet_direction = 1

		self.alien_limits = 4

		#加快游戏的节奏
		self.speedup_scale = 1.1
		self.number_scale = 2
		self.initialize_dynamic_settings()

		#计分
		self.alien_points = 50
		self.score_scale = 1


	def initialize_dynamic_settings(self):
		"""初始化随游戏进行而变化的设置"""
		self.ship_speed = 0.8
		self.bullet_speed = 1
		self.alien_speed = 0.2
		self.alien_limits = 4
		self.fleet_direction = 1


	def increase_speed(self):
		"""提高速度设置"""
		self.ship_speed *= self.speedup_scale
		self.bullet_speed *= self.speedup_scale
		self.alien_speed *= self.speedup_scale

		if self.alien_limits * self.number_scale <= 55:
			self.alien_limits *= self.number_scale
		else:
			self.alien_limits = 55