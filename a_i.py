#! /usr/bin/python3

import sys
import pygame
from pygame.sprite import Sprite

class Settings():
	'''
		All configurable parameters are stored here.
	'''
	def __init__(self):
		self.screen_width=1200
		self.screen_height=800
		self.bg_color=230,230,230

class Ship(Sprite):
	'''
		Settings for main battle ship
	'''
	def __init__(self, ai_settings, screen):
		super(Ship, self).__init__()
		self.screen=screen
		self.ai_settings=ai_settings
		self.image=pygame.image.load('images/ship.bmp').convert()
		self.image.set_colorkey((230, 230, 230))
		self.rect=self.image.get_rect()
		self.screen_rect=self.screen.get_rect()
		self.rect.centerx=self.screen_rect.centerx
		self.rect.bottom=self.screen_rect.bottom
		self.center=float(self.rect.centerx)
		self.moving_right=False
		self.moving_left=False
	def update(self):
		pass
	def blitme(self):
		self.screen.blit(self.image, self.rect)
	def center_ship(self):
		self.center = self.screen_rect.centerx

def run_game():
	pygame.init()
	ai_settings=Settings()
	screen=pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	ship=Ship(ai_settings, screen)
	while True:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				sys.exit()
		ship.update()
		screen.fill(ai_settings.bg_color)
		ship.blitme()
		pygame.display.flip()


run_game()
