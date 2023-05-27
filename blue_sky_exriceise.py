import sys
import pygame

class Screen():
	def __init__(self):
		self.screen_hight = 1000
		self.screen_width = 800
	
	def check_event():
		for event in pygame.event.get():
			if event.type == pygame.QUIT:		
				sys.exit()	
