import shelve

class GameStats():
	"""Track statistics for Alien Invasion."""
	
	def __init__(self, ai_settings):
		"""Initalize statistics."""
		self.ai_settings = ai_settings
		self.reset_stats()
		
		# Start game in an inactive state.
		self.game_active = False 
		
		# High score should never be reset.
		self.high_score = 0
		
		# I TRY SOMETHING
		d = shelve.open("all_time_score.txt")
		self.high_score = d["all_time_score"]
		
	def reset_stats(self):
		"""Initialize statistics that can change during the game."""
		self.ships_left = self.ai_settings.ship_limit	
		self.score = 0
		self.level = 1
		
		
