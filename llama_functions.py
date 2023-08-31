
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

def llama_jump(loop,jumping):
	'''
 	jump function grabs the loop number, llama’s start height, llama’s jump height
	
	'''
	up_allowed = False
	if loop == 0 and jumping:
		for i in range(1,c.LLAMA_JUMP_HEIGHT):
			llama_y = c.LLAMA_Y_START - i
			
			
		jump_loop = 1

	elif loop >= 1:
		if loop > c.LLAMA_JUMP_DURATION:
			jump_loop = 0
			llama_y = c.LLAMA_Y_START
			up_allowed = True

		else:
			jump_loop = loop + 1 
			llama_y = c.LLAMA_Y_START - c.LLAMA_JUMP_HEIGHT
	elif loop == 0 and not jumping:
		jump_loop = 0
		llama_y = c.LLAMA_Y_START
		up_allowed = True
	return llama_y,jump_loop,up_allowed 