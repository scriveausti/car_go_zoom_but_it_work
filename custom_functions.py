#-------------------------#
#          								#
#		custom Functions			#
#		Made By Austin				#
#		date:									#
#													#
#-------------------------#

import config as c
import general_functions as fun

#-------------------------#


def player_movement(player, up, down):
	'''
	Takes the user input variables and check if they are true if so the
 	players will move in that direction. E.G. If the up key is pressed
	it will move the players car up thus decressing the lane number bc
 	lane numbers go 1 at top then they decress as they go down.
	'''

	player['lane'] = player['lane']

	if up and player['lane'] > 1:
		player['lane'] = player['lane'] - 1

	elif down and player['lane'] < c.amount_of_lanes:
		player['lane'] = player['lane'] + 1

	return player['lane']


def game_reset(player, enemycars):
	'''
 	Resets the variables of the players car, enemy cars and the score to
	there starting values or random ones if so needed. 
 	'''
	player = {
	 'x': c.SCREEN_WIDTH / 3,
	 'y': c.lanes_y[1],
	 'colour': 'blue',
	 'size_x': 40,
	 'size_y': 20,
	 'lane': 1,
	 'dead': False
	}
	for i in enemycars:
		i.reset()

	score = 0
	return player, enemycars, score
