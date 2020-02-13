#re_high_score.py
import json


class High_score_loader():
	
	def __init__(self,stats):
		'''загружает рекорд. Если не было до этого - записывает.'''
		self.file_name = 'high_score.json'
		self.stats = stats
		try:
			with open(self.file_name) as self.fo:
				self.high_score = json.load(self.fo)
				
		except FileNotFoundError:
			self.write_high_score()
			
		else:
			if self.high_score > stats.high_score:
				stats.high_score = self.high_score
			else:
				self.write_high_score()
				
	def write_high_score(self):
		with open(self.file_name, 'w') as fo:
			high_score = self.stats.high_score
			json.dump(high_score, fo)
			
			
