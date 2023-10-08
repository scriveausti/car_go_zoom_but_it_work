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



# pygame setup 
pygame.init()
font = pygame.font.SysFont("Comic Sans MS", 40)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(WINDOW_NAME)

# loads the game icon 
# but if the icon can't be then will give an error message 
try:
	game_icon = pygame.image.load('game_icon.png')
	pygame.display.set_icon(game_icon)
except:
	print("game icon not loaded")

for i in range(0, amount_of_objects):
	enemycars.append(enemy_car(i))


def message_center(msg, text_colour, bkgd_colour):
	'''
	displays a text box in the middle of the screen
	'''
	txt = font.render(msg, True, text_colour, bkgd_colour)
	center_of_screen = fun.get_middle_screen()
	text_box = txt.get_rect(center=center_of_screen)
	screen.blit(txt, text_box)


for i in range(0, amount_of_car_images):
	car_file_name = "car_{}.png".format(i + 1)
	try:
		car_icon_not_resized = (pygame.image.load(car_file_name).convert_alpha())
		car_icon_not_resized = pygame.transform.rotate(car_icon_not_resized, 270)
		car_icons.append(
		 pygame.transform.smoothscale(
		  car_icon_not_resized, [ostacle_specs['width'], ostacle_specs['height']]))
		print("loaded file " + str(car_file_name))

	except:
		print("failed to load file " + str(car_file_name))
		message_center("failed to load " + str(car_file_name),
		               colours[error_message_colours], None)

while has_not_quit:
	restart = False
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

			if event.key == pygame.K_r:
				restart = True

			elif event.key == pygame.K_q:
				has_not_quit = False

		else:
			up = False
			down = False

	if playing:
		player['lane'] = cfun.player_movement(player, up, down)
		player['y'] = lanes_y[player['lane']]

		# background
		screen.fill(colours[background_colour])
		
		# ground being drawn
		pygame.draw.rect(screen, colours[GROUND_COLOUR],
		                 [GROUND_X, GROUND_Y, GROUND_WIDTH, GROUND_HEIGHT])

		for i in range(0, amount_of_objects):
			player, score = enemycars[i].update(screen, player, score, car_icons)

		# players car being drawn
		player_car = pygame.draw.rect(
		 screen, colours[player['colour']],
		 [player['x'], player['y'], player['size_x'], player['size_y']])
		screen.blit(car_icons[5], player_car)

		display_score = int(score)

		# checks if score is higher then the highscore
		# if it is rewrites the highscore file
		if display_score > highscore:
			highscore_file = open('highscore.txt', 'w')
			highscore_file.write(str(display_score))
			highscore_file.close()
			highscore = display_score

		# displays highscore and score in at the top of the screen
		fun.score_ui(screen, display_score, highscore, font)
		fun.screen_update()
		if player['dead']:
			playing = False

	# asks if the user wants to resatrt or quit 
	else:
		if restart:
			playing = True
			player, enemycars, score = cfun.game_reset(player, enemycars)
		msg = "Press R to resatrt, Press Q to Quit"
		message_center(msg, colours[end_screen_text_colour], None)
		fun.screen_update()

pygame.quit()
