import sys
import pygame
from blue_sky_exriceise import Screen

def blue_screen():
	pygame.init()
	surface = Screen()
	screen = pygame.display.set_mode((surface.screen_hight,
										surface.screen_width))
	bg_color = (0, 0, 255)
	
	while True:
		Screen.check_event()
		
		screen.fill(bg_color)
		pygame.display.flip()

blue_screen()	
