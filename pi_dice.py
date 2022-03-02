from random import random
##dice rolling optomized
def dice3():
	r0 = random()
	if r0 <= 1/3:
		d0 = (1)
	elif r0 <= 2/3:
		d0 = (2)
	else:
		d0 = (3)
	return (d0)
def dice6():
	r0 = random()
	if r0 <= 1/6:
		d0 = (1)
	elif r0 <= 2/6:
		d0 = (2)
	elif r0 <= 3/6:
		d0 = (3)
	elif r0 <= 4/6:
		d0 = (4)
	elif r0 <= 5/6:
		d0 = (5)
	else:
		d0 = (6)
	return (d0)