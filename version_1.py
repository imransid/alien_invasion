import sys

import pygame

from setting import Setting
from  ship import Ship

def run_game():
	pygame.init()
	ai_setting = Setting()
	screen = pygame.display.set_mode((ai_setting.screen_width, ai_setting.screen_height))
	pygame.display.set_caption("Alien Invasion")

	# make a ship
	ship = Ship(screen)

	while True:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

			screen.fill(ai_setting.bg_color)

			ship.blitme()

			pygame.display.flip()

run_game()