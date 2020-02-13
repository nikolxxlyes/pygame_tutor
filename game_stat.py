#game_stat.py
from re_high_score import High_score_loader
 
class GameStats():
	"""Отслеживание статистики для игры Alien Invasion."""
	
	def __init__(self, ai_settings):
		"""Инициализирует статистику."""
		self.ai_setttings = ai_settings
		self.reset_stats()
		
		# Игра Alien Invasion запускается в активном состоянии.
		self.game_active = False
		self.high_score = 0
		High_score_loader(self)
		
	def reset_stats(self):
		"""Инициализирует статистику, изменяющуюся в ходе игры."""
		self.ship_left = self.ai_setttings.ship_limit
		self.score = 0
		self.level = 1
		
