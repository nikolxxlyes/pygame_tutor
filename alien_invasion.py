#alien_invasion.py
import pygame
import game_function as gf

from pygame.sprite import Group
from settings import Settings
from ship import Ship
from game_stat import GameStats
from buttom import Button
from scoreboard import ScoreBoard
def run_game():
	'''Инициализирует игру, настройки и создает обьект экрана.'''
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("Alient Invasion")
	
	# Создание кнопки Play.
	play_button = Button(ai_settings, screen, "Play")
	# Создание экземпляров GameStats и Scoreboard.
	stats = GameStats(ai_settings)
	sb = ScoreBoard(ai_settings, screen, stats)
	#Создание корабля
	ship = Ship(ai_settings, screen)
	# Создание группы для хранения пуль.
	bullets = Group()
	# Создание пришельца.
	aliens = Group()
	

	# Создание флота пришельцев.
	gf.create_fleet(ai_settings, screen, ship, aliens)
	#Запуск основного цикла игры
	while True:
		gf.check_events(ai_settings, screen, stats, sb, play_button, 
		ship, bullets, aliens)
		if stats.game_active:
			ship.update()
			gf.update_bullets(ai_settings, screen, ship, stats, sb,
						aliens,	bullets)
			gf.update_aliens(ai_settings,screen,stats, sb, ship, aliens,
						bullets)
		gf.update_screen(ai_settings, screen, stats,sb, ship, aliens, 
					bullets, play_button)
run_game()
