#settings.py

class Settings():
	'''
	Класс для хранения всех настроек игры.
	'''
	def __init__(self):
		"""Инициализирует статические настройки игры."""
		#Параметры экрана
		self.screen_width = 1720
		self.screen_height = 900
		self.bg_color = (230, 230, 230)
		self.bullet_height = 15
		self.bullet_color = 60,60,60
		#переключение управления на левую клавиатуру 1,стрелки(0)
		self.keybords_type = 1
		# Темп ускорения игры
		self.speedup_scale = 1.1
		self.score_scale = 1.1
		self.initialize_dynamic_settings()
		
	def initialize_dynamic_settings(self):
		"""Инициализирует настройки, изменяющиеся в ходе игры."""
		self.ship_speed_factor = 2.2
		self.alien_speed_factor = 1.2
		self.bullet_speed_factor = 2.3
		self.bullet_allowed = 3
		self.bullet_width = 3
		self.fleet_drop_speed = 10
		self.ship_limit = 3
		# fleet_direction = 1 обозначает движение вправо; а -1 - влево.
		self.fleet_direction = 1
		# Подсчет очков
		self.alien_points = 50
		
	def increase_speed(self):
		"""Увеличивает настройки скорости."""
		#self.ship_speed_factor *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale 
		self.bullet_speed_factor *= self.speedup_scale
		#self.fleet_drop_speed += 10
		if not self.bullet_allowed == 6:
			self.bullet_allowed += 1
		#self.bullet_width += 3 
		self.alien_points = int(self.score_scale * self.alien_points)
