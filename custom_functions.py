
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

def player_movement(player,up,down):
	'''

	
	'''
	
	player['lane'] = player['lane']
	if up and player['lane']>1:
		player['lane'] = player['lane'] - 1 
	elif down and player['lane']< c.amount_of_lanes:
		player['lane'] = player['lane'] + 1 
	return player['lane']