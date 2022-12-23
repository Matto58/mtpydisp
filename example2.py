"""
Another example program using PyDisp.
"""

# Matto's PyDisp - example 2
# version v0.1.0
#
# Licensed under MPL v2.0
# https://github.com/Matto58/mtpydisp

from mtpydisp	import PyDisp			# Import the PyDisp class
from pygame		import event, QUIT		# Get pygame.event & pygame.QUIT so the app doesn't crash on first run
from random		import randint			# Import the randint function

import time 							# Import the time module to time the first frame of the render

display = PyDisp().new((50, 50), 15)	# Create a new PyDisp with resolution 50x50 and a scale of 15

t = 0		# Time in frames (initiated with 0)
fps = 60	# Max frames per second

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

	# Start timer
	tm = time.time()

	# Fill the display with random pixels
	RandomPixels(50, 50)

	# Update display, time the render process every 10 frames, wait for 1/fps seconds and increment t
	display.update()
	if t % 10 == 9: print(f"Frame #{t + 1}:\t{round(time.time() - tm, 4)}s")
	PyDisp.wait(fps)
	t += 1
