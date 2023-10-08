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
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800

framerate = 60

#-----------------------------#

playing = True
has_not_quit = True



up_allowed = True
down_allowed = True

up = False

jump_loop = 0

background_colour = 'green'


error_message_colours = 'red'
end_screen_text_colour = 'white'

amount_of_car_images = 6

#-----------------------------#
#background constances and variables

GROUND_COLOUR = 'dark gray'
GROUND_HEIGHT = (SCREEN_HEIGHT / 3) * 2
GROUND_WIDTH = SCREEN_WIDTH * 2
GROUND_X = 0
GROUND_Y = SCREEN_HEIGHT / 6

#-----------------------------#
player_size_y = 20
amount_of_lanes = 5

lanes_y = {}

lane_base_y = ((GROUND_HEIGHT ) / amount_of_lanes)
lane_base_y = ((GROUND_HEIGHT -(lane_base_y/2) ) / amount_of_lanes)
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

ostacle_speed_min = 2
max_object_speed_multi = 3

amount_of_objects = 5 # can go up to 6 but one car will
# be the same colour as the player 

ostacle_specs = {
 'start_x': SCREEN_WIDTH - 20,
 'x': SCREEN_WIDTH - 20,
 'lane': 1,
 'width': 40,
 'height': 20,
 'colour': 'red',
 'speed multi': 1
}

car_icons = []
enemycars = []


#-----------------------------#

score = 0
highscore = 0
highscore_loop = True


while highscore_loop:
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

