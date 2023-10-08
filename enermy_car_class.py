import config as c
import random
from colours import colours
import pygame


class enemy_car:
	'''
 	Class for spawning and running the enemy cars
 	'''

	def __init__(self, carnumber):
		self.width = c.ostacle_specs['width']
		self.height = c.ostacle_specs['height']
		self.colour = c.ostacle_specs['colour']
		self.has_been_scored = False
		self.carnumber = carnumber
		self.lane = (random.randint(1, c.amount_of_lanes))
		self.speed_multi = (random.randint(10, (c.max_object_speed_multi * 10)) / 10)
		self.x = c.SCREEN_WIDTH + random.randint(20, 200)
		self.y = c.lanes_y[self.lane]

	def off_screen(self):
		"""
		Should be ran when the car goes off screen (when x < 0).
		Resets the cars x pos with a random off set to give the feeling
		like there is a delay between going off screen and respawning.
		Also randomises the lane that the car is in.
		Resets the has_been_scored variable aswell.
		"""
		self.lane = (random.randint(1, c.amount_of_lanes))
		self.y = c.lanes_y[self.lane]
		self.x = c.SCREEN_WIDTH + random.randint(20, 200)
		self.speed_multi = (random.randint(10, (c.max_object_speed_multi * 10)) / 10)
		self.has_been_scored = False

	def draw(self, screen, car_icons):
		'''
		Draws the car on screen once the screen is updated.
 		'''

		car = pygame.draw.rect(screen, colours[self.colour],
		                       [self.x, self.y, self.width, self.height])
		try:
			screen.blit(car_icons[self.carnumber], car)
		except:
			print('failed to join car image with hitbox')

	def movement(self):
		'''
		Moves the enemy car to the left based on the obstacle speed set in
 		config and by the cars speed mutilplyer.
 		'''
		self.x = int(self.x - (c.ostacle_speed_min * self.speed_multi))

	def collition(self, player):
		'''
		Checks if the player car hits an enemy car. 
 		If it is then it sets the players dead statuse to true. 
		'''
		if player['lane'] == self.lane and self.x > player['x'] > self.x - self.width:
			player['dead'] = True
			print('car hit')
			return player
		else:
			return player

	def score_calculation(self, player, score):
		"""
		checks if the car has been scored on before. If it hasn't
		been then it will check if the players car is in the same x values as it self
		"""

		if not self.has_been_scored:
			if self.x > player['x'] > self.x - self.width:
				score = score + 1
				self.has_been_scored = True
		return score

	def update(self, screen, player, score, car_icons):
		"""
		Updates the cars X, draws it, checks collition, checks score and
		check if the car is off screen.
		"""
		self.movement()
		self.draw(screen, car_icons)
		player = self.collition(player)
		score = self.score_calculation(player, score)

		if self.x < 0:
			self.off_screen()

		return player, score

	def reset(self):
		"""
		Runs when the programe is resestting.
		Resets all variables to what they should be at a starting pos.
		"""
		self.width = c.ostacle_specs['width']
		self.height = c.ostacle_specs['height']
		self.colour = c.ostacle_specs['colour']
		self.has_been_scored = False
		self.lane = (random.randint(1, c.amount_of_lanes))
		self.speed_multi = (random.randint(10, (c.max_object_speed_multi * 10)) / 10)
		self.x = c.SCREEN_WIDTH + random.randint(20, 200)
		self.y = c.lanes_y[self.lane]
