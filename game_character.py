import sys
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
title = pygame.display.set_caption("Son Kogu")
bg_color = (255, 255 , 255)
image = pygame.image.load('images/kogu.bmp')
image_rect = image.get_rect()
screen_rect = screen.get_rect()
image_rect.centerx = screen_rect.centerx


	
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		
	screen.fill(bg_color)
	screen.blit(image, image_rect)
	pygame.display.flip()
	
		
				
