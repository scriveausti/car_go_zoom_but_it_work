import config as c
import random
from colours import colours
import pygame


class enemy_car:

	def __init__(self):
		self.start_x = c.ostacle_specs['start_x']
		self.x = c.ostacle_specs['x']
		self.lane = c.ostacle_specs['lane']
		self.width = c.ostacle_specs['width']
		self.height = c.ostacle_specs['height']
		self.colour = c.ostacle_specs['colour']
		self.speed_multi = c.ostacle_specs['speed multi']
		self.y = c.lanes_y[self.lane]

	def off_screen(self):
		self.lane = (random.randint(1, c.amount_of_lanes))
		self.y = c.lanes_y[self.lane]
		self.x = c.SCREEN_WIDTH + random.randint(20, 200)
		self.speed_multi = (random.randint(10, (c.max_object_speed_multi * 10)) / 10)

	def draw(self, screen):
		pygame.draw.rect(screen, colours[self.colour],
		                 [self.x, self.y, self.width, self.height])

	def movement(self):
		self.x = self.x - (c.ostacle_speed * self.speed_multi)
