
#-----------------------#
#          							#
#		Basic Functions			#
#		Made By Austin			#
#		date:								#
#												#
#-----------------------#

import pygame
from colours import colours
import config as c
import ui_config as ui

#-------------------------------------------------------#

def get_screen_size():
  """
  this gives the screen width and height
  outputs a tulip (screen_width,screen_height)
  """
  return pygame.display.get_window_size()

#-------------------------------------------------------#

def get_middle_screen():
  """
  This returns the x and y positions of the middle of the output
	screen
  outputs a tulip (middle_x, middle_y)
  """
  screen_width, screen_height = get_screen_size()
  middle_of_screen = (screen_width / 2, screen_height / 2)

  return middle_of_screen

#-------------------------------------------------------#

def screen_update():
  '''
	updates screen 
  '''
  clock = pygame.time.Clock()
  pygame.display.update()
  clock.tick(c.framerate)

#-------------------------------------------------------#

def none_check(input):
	'''
	checks if the inpu is set to None (not blank but None) 
 	outputs True or False 
	'''
	if input == None:
		return True
	else:
		return False

#-------------------------------------------------------#

def colour_none_checker(colour):
	'''
 	checks if the input is set to a colour or None
 	'''
	if not none_check(colour):
		return colours[colour]
	else:
		return None

#-------------------------------------------------------#

def score_ui(screen,score,highscore,font):
	"""
	displays score and highscore in top left and top right
	"""
	#draw score 
	ui_text(screen,('score: {}'.format(score)), 'topleft',font)
	
	#draw highscore
	ui_text(screen,('highscore: {}'.format(highscore)), 'topright',font)
	
#-------------------------------------------------------#

def ui_text(screen,message,corner,font):
	'''
 	renders text form a corner 
	currnt definded corners are "topright" & "topleft"
 	'''
	txt = font.render(message, True, ui.text_colour, ui.background_colour)
	screen_width, screen_height = get_screen_size()
	if corner == 'topright':
		text_box = txt.get_rect(topright=((screen_width - ui.space_from_border),ui.space_from_border))
	elif corner == 'topleft':
		text_box = txt.get_rect(topleft=((0 + ui.space_from_border),ui.space_from_border))
	screen.blit(txt, text_box)

#-------------------------------------------------------#



