import pygame
import random

#imports general uses functions
import general_functions as fun

#imports custom functions
import custom_functions as cfun

#colour lib
from colours import colours

#imports all the variables that are used in the program
from config import *

#imports all the keyind variables
from keybinds import *

pygame.init()
font = pygame.font.SysFont("comicsans", 40)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT),
                                 pygame.RESIZABLE)
pygame.display.set_caption(WINDOW_NAME)

while playing:
	for event in pygame.event.get():
		# when the window is resized the screen width and height are updated
		if event.type == pygame.WINDOWRESIZED:
			SCREEN_WIDTH, SCREEN_HEIGHT = fun.get_screen_size()

		if event.type == pygame.QUIT:
			playing = False

		# llama movement
		if event.type == pygame.KEYDOWN:

			if event.key in up_keys and up_allowed:
				up = True
				down = False

			elif event.key in down_keys and down_allowed:
				up = False
				down = True

			else:
				up = False
				down = False

		else:
			up = False
			down = False

	player['lane'] = cfun.player_movement(player, up, down)
	player['y'] = lanes_y[player['lane']]

	#background
	screen.fill(colours[background_colour])
	#ground being drawn
	pygame.draw.rect(screen, colours[GROUND_COLOUR],
	                 [GROUND_X, GROUND_Y, GROUND_WIDTH, GROUND_HEIGHT])

	for i in range(0, amount_of_objects):
		ostacles[i]['y'] = lanes_y[ostacles[i]['lane']]
		pygame.draw.rect(screen, colours[ostacles[i]['colour']], [
		 ostacles[i]['x'], ostacles[i]['y'], ostacles[i]['width'],
		 ostacles[i]['height']
		])

		ostacles[i]['x'] = ostacles[i]['x'] - (ostacle_speed *
		                                       ostacles[i]['speed multi'])

		if ostacles[i]['x'] < 0:
			ostacles[i]['lane'] = (random.randint(1, amount_of_lanes))
			ostacles[i]['x'] = SCREEN_WIDTH + random.randint(20, 200)
			ostacles[i]['speen multi'] = (
			 random.randint(1, max_object_speed_multi * 10) / 10)

		print('object speed multi ='+ str(ostacles[i]['speed multi']))
		print('object lane =' + str(ostacles[i]['lane']))
		print('player lane =' + str(player['lane']))
		print('object x =' + str(ostacles[i]['x']))
		print('player x =' + str(player['x']))

		print('same_lane =' + str(ostacles[i]['lane'] == player['lane']))
		print('in hitbox =' +
		      str(player['x'] < ostacles[i]['x'] < player['x'] + player['size_x']))

		if (ostacles[i]['lane'] == player['lane']) and (
		  player['x'] < ostacles[i]['x'] < player['x'] + player['size_x']):
			llama_dead = True
			score = 0
			print('player dead')
		elif (player['x'] < ostacles[i]['x'] < player['x'] + player['size_x']):
			score = score + 1
			print('score +1')

	#llama being drawn
	pygame.draw.rect(
	 screen, colours[player['colour']],
	 [player['x'], player['y'], player['size_x'], player['size_y']])

	display_score = int(score * score_multipyer)

	if display_score > highscore:
		highscore_file = open('highscore.txt', 'w')
		highscore_file.write(str(display_score))
		highscore_file.close()
		highscore = display_score

	fun.score_ui(screen, display_score, highscore, font)
	fun.screen_update()

pygame.quit()
