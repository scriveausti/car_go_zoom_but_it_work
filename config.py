#---------------------------#
#          									#
#		config to be imported		#
#		Made By Austin					#
#		date:										#
#														#
#---------------------------#

import pygame
import random
#---------------------------------------------------------------#

WINDOW_NAME = " car go zoom "
SCREEN_HEIGHT = 300
SCREEN_WIDTH = 400

framerate = 60

#-----------------------------#

playing = True

up_allowed = True
down_allowed = True

up = False

jump_loop = 0


background_colour = 'green'

#-----------------------------#
#background constances and variables

GROUND_COLOUR = 'dark gray'
GROUND_HEIGHT = (SCREEN_HEIGHT / 3) * 2
GROUND_WIDTH = SCREEN_WIDTH * 2
GROUND_X = 0
GROUND_Y = SCREEN_HEIGHT / 6

#-----------------------------#
player_size_y = 20
amount_of_lanes = 20
lanes_y = {}
lane_base_y = ((GROUND_HEIGHT - player_size_y) / amount_of_lanes)

for i in range(1, (amount_of_lanes + 1)):
	srt_i = (i)
	lanes_y[srt_i] = ((lane_base_y) * i) + GROUND_Y

print(lanes_y)

#-----------------------------#

#llama constances & variables

player = {
 'x': SCREEN_WIDTH / 3,
 'y': lanes_y[1],
 'colour': 'blue',
 'size_x': 40,
 'size_y': 20,
 'lane': 1,
 'dead': False
}

#-----------------------------#

ostacle_speed = 2
ostacle_same_x = {}
max_object_speed_multi = 3

amount_of_objects = 2
# somehow incresses speed of objects idk how

ostacle_specs = {
 'start_x': SCREEN_WIDTH - 20,
 'x': SCREEN_WIDTH - 20,
 'lane': 1,
 'width': 40,
 'height': 20,
 'colour': 'red',
 'speed multi': 1
}

enemy_cars = []

score = 0


highscore = 0

highscore_loop = True

try:
	highscore_file = open('highscore.txt', 'x')
	highscore_file = open('highscore.txt', 'r+')
	print('part 1 working')
except:
	highscore_file = open('highscore.txt', 'r+')
	print('part 2 working')
while highscore_loop:
	try:
		highscore = int(highscore_file.read())
		highscore_loop = False
		print('part 3 working')

	except:
		highscore_file.write(str(0))
		highscore = int(highscore_file.read())
		highscore_loop = False
		print('part 4 working')
highscore_file.close()
