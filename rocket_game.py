import pygame

from rocket_settings import Rocket_Settings
from rocket import Rocket
import rocket_game_functions as gf

def run_game():		
	#Initialize pygame, settings, and screen object.
	pygame.init()
	ai_settings = Rocket_Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Rocket")
	
	# Make a rocket
	rocket = Rocket(ai_settings, screen)
	
	# Start the main loop for the game.
	while True:
		gf.check_events(rocket)
		rocket.update()
		gf.update_screen(ai_settings, screen, rocket)

run_game()		
		 	
