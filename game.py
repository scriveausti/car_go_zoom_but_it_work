import pygame
import random

from enermy_car_class import enemy_car


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
font = pygame.font.SysFont("Comic Sans MS", 40)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT),
                                 pygame.RESIZABLE)
pygame.display.set_caption(WINDOW_NAME)
game_icon = pygame.image.load('game_icon.png')
pygame.display.set_icon(game_icon)



enemy_1 = enemy_car()
enemy_2 = enemy_car()
enemy_3 = enemy_car()
enemy_4 = enemy_car()

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


	
	enemy_1.draw(screen)
	enemy_1.movement()

	enemy_2.draw(screen)
	enemy_2.movement()

	enemy_3.draw(screen)
	enemy_3.movement()

	enemy_4.draw(screen)
	enemy_4.movement()
	
	if enemy_1.x < 0:
		enemy_1.off_screen()
	if enemy_2.x < 0:
		enemy_2.off_screen()
	if enemy_3.x < 0:
		enemy_3.off_screen()
	if enemy_4.x < 0:
		enemy_4.off_screen()
		

		#if (obstacle['lane'] == player['lane']) and (
		  #player['x'] < obstacle['x'] < player['x'] + player['size_x']):
			#llama_dead = True
			#score = 0
			#print('player dead')
		#elif (player['x'] < obstacle['x'] < player['x'] + player['size_x']):
			#score = score + obstacle['speed multi']
			#print('score +1')
		#obstacles_i = obstacles_i + 1


	
	#llama being drawn
	pygame.draw.rect(
	 screen, colours[player['colour']],
	 [player['x'], player['y'], player['size_x'], player['size_y']])


	
	display_score = int(score) #* score_multipyer)

	if display_score > highscore:
		highscore_file = open('highscore.txt', 'w')
		highscore_file.write(str(display_score))
		highscore_file.close()
		highscore = display_score

	fun.score_ui(screen, display_score, highscore, font)
	fun.screen_update()

pygame.quit()
