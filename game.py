import pygame
import random

#imports general uses functions 
import general_functions as fun

#imports custom functions 
import llama_functions as cfun


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

def obsitcal():
	'''
 	'''
	


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
				up_allowed = False
				down_allowed = True
				
			
			elif event.key in down_keys and down_allowed:
				down = True

		else:
			up = False 
	llama_y,jump_loop,up_allowed = cfun.llama_jump(jump_loop,up)
	
	screen.fill(colours[background_colour])
	
	pygame.draw.rect(screen,colours[ostacle_1['colour']],
	[ostacle_1['x'],ostacle_1['y'],ostacle_1['width'],ostacle_1['height']])
	pygame.draw.rect(screen,colours[ostacle_2['colour']],
	[ostacle_2['x'],ostacle_2['y'],ostacle_2['width'],ostacle_2['height']])

	ostacle_1['x'] = ostacle_1['x'] - ostacle_speed
	
	if ostacle_1['x'] < 0:
		ostacle_1['x'] = SCREEN_WIDTH + random.randint(20,200)


	
	ostacle_2['x'] = ostacle_2['x'] - ostacle_speed
	
	if ostacle_2['x'] < 0:
		ostacle_2['x'] = SCREEN_WIDTH + random.randint(100,200)

	ostacle_1_same_x = ( LLAMA_X > ostacle_1['x'] > LLAMA_X - llama_hitbox_size)
	ostacle_2_same_x = ( LLAMA_X > ostacle_2['x'] > LLAMA_X - llama_hitbox_size)
	if (( ostacle_1_same_x or ostacle_2_same_x ) and llama_y >= LLAMA_Y_START):
		llama_dead = True 
		score = 0 
		print('dead')
	elif ( ostacle_1_same_x or ostacle_2_same_x): 
		score = score + 1
		print('+1')

	
	#ground being drawn
	pygame.draw.rect(screen,colours[GROUND_COLOUR],
	[GROUND_X,GROUND_Y,GROUND_WIDTH,GROUND_HEIGHT])
	#llama being drawn
	pygame.draw.rect(screen,colours[LLAMA_COLOUR],
	[LLAMA_X,llama_y,LLAMA_SIZI,LLAMA_SIZI])
	
	display_score = int(score*score_multipyer)

	if display_score > highscore:
		highscore_file = open('highscore.txt','w')
		highscore_file.write(str(display_score))
		highscore_file.close()
		highscore = display_score
  
	fun.score_ui(screen,display_score,highscore,font)
	fun.screen_update()

pygame.quit()