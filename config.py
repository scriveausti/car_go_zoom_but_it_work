
#---------------------------#
#          									#
#		config to be imported		#
#		Made By Austin					#
#		date:										#
#														#
#---------------------------#

import pygame

#---------------------------------------------------------------#

WINDOW_NAME = " Llama Run "
SCREEN_HEIGHT = 300
SCREEN_WIDTH = 400

framerate = 60

#-----------------------------#

playing = True

up_allowed = True
down_allowed = True

up = False



jump_loop = 0

#-----------------------------#

#llama constances & variables 

llama_y = SCREEN_WIDTH / 2 
LLAMA_X = SCREEN_WIDTH/3
LLAMA_Y_START = llama_y
LLAMA_JUMP_HEIGHT = 40
LLAMA_COLOUR = 'green'
LLAMA_SIZI = 20
LLAMA_JUMP_DURATION = 40


llama_hitbox_size = 20

llama_dead = False 

#-----------------------------#

#background constances and variables 

GROUND_COLOUR = 'dark gray'
GROUND_HEIGHT = SCREEN_HEIGHT / 2
GROUND_WIDTH = SCREEN_WIDTH*2
GROUND_X = 0
GROUND_Y = LLAMA_Y_START + LLAMA_SIZI

#-----------------------------#

ostacle_speed = 2

ostacle_1 = {
	'start_x': SCREEN_WIDTH + 20,
	'x': SCREEN_WIDTH + 20 ,
	'y': LLAMA_Y_START,
	'width': 20,
	'height': 30,
	'colour':'red'
	
}
ostacle_2 = {
	'start_x': SCREEN_WIDTH + 20,
	'x': SCREEN_WIDTH + 60,
	'y': LLAMA_Y_START,
	'width': 20,
	'height': 30,
	'colour':'red'
}


background_colour = 'green'



score = 0
score_multipyer = ostacle_speed/ostacle_1['width']

highscore = 0


highscore_loop = True

try:
    highscore_file = open('highscore.txt','x')
    highscore_file = open('highscore.txt','r+')
    print('part 1 working')
except:
    highscore_file = open('highscore.txt','r+')
    print('part 2 working')
while highscore_loop:
  try:
    highscore = int(highscore_file.read())
    highscore_loop = False
    print('part 3 working')
  
  except :
    highscore_file.write(str(0))
    highscore = int(highscore_file.read())
    highscore_loop = False
    print('part 4 working')
highscore_file.close()

