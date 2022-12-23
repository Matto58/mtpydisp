"""
An example program using PyDisp.
"""

# Matto's PyDisp - example
# version v0.1.0
#
# Licensed under MPL v2.0
# https://github.com/Matto58/mtpydisp

from mtpydisp	import PyDisp			# Import the PyDisp
from pygame		import event, QUIT		# Get pygame.event & pygame.QUIT so the app doesn't crash on first run
from random		import randint			# Import the randint function

display = PyDisp().new((160, 100), 6)	# Create a new PyDisp with resolution 160x100 and a scale of 6

t = 0		# Time in frames (initiated with 0)
fps = 15	# Max frames per second

def RandomPixels(xsize: int, ysize: int):
	"""Fill the display with random pixels within the range (0, 0) -> (xsize, ysize)."""
	for y in range(ysize):
		for x in range(xsize):
			display.setPx(x, y, randint(0, 15))


# Loop forever
while True:
	# Get the events & quit accordingly (required to work properly)
	for e in event.get():
		if e.type == QUIT: exit(0)

	# Fill the background with dark blue
	display.setBG(4)

	# Make a rectangle starting at (20, 11), with the size of (30, 12) and the color green
	display.drawRect(10, (20, 11, 30, 12))

	# Fill the top (16, 9) pixels with random colors
	RandomPixels(16, 9)

	# Update display, wait for 1/fps seconds and increment t
	display.update()
	PyDisp.wait(fps)
	t += 1
