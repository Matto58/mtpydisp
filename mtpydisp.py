"""
A 16-color virtual pixel display.
"""

# Matto's PyDisp
# version v0.1.0
#
# Licensed under MPL v2.0
# https://github.com/Matto58/mtpydisp

from pygame import draw, display
from pygame.surface import Surface
from pygame.time import Clock

_ver: str = "0.1.0"

print(f"\nMatto's PyDisp, version v{_ver}\nContribute at https://github.com/Matto58/mtpydisp")

class PyDisp:
	scr: Surface = None
	settings: dict = None
	_pxs: list[list[int]] = None
	_v = _ver

	_clr = [
		(000, 000, 000), (127, 127, 127), (191, 191, 191), (255, 255, 255),
		(000, 000, 127), (255, 000, 000), (255, 255, 000), (255, 000, 255),
		(000, 127, 127), (000, 127, 000), (000, 255, 000), (000, 255, 255),
		(127, 000, 127), (127, 127, 000), (127, 000, 000), (000, 127, 000)
	]

	def setPx(self, x: int, y: int, color: int):
		if x < self.settings["resolutionX"] and y < self.settings["resolutionY"]:
			if x >= 0 and y >= 0:
				if color >= 0 and color < 16:
					self._pxs[x][y] = color

	def getPx(self, x: int, y: int) -> int:
		if x < self.settings["resolutionX"] and y < self.settings["resolutionY"]:
			if x >= 0 and y >= 0:
				return self._pxs[x][y]

	def setBG(self, color: int):
		x = 0
		for row in self._pxs:
			y = 0
			for px in row:
				self.setPx(x, y, color)
				y += 1
			x += 1
				

	def update(self, doRead: bool = True, doWrite: bool = True):
		if doRead: self._readPxsFromFl()

		(x,y) = (0,0)
		s = self.settings["scale"]
		for row in self._pxs:
			for px in row:
				draw.rect(self.scr, self._clr[px], (x,y , s,s))
				y += s

			x += s
			y = 0

		if doWrite: self._savePxsToFl()
		

	def _savePxsToFl(self, fl: str = "pydisp"):
		_f = bytearray()

		for row in self._pxs:
			for px in row:
				_f.append(px)

		_fl = open(fl, "wb")
		_fl.write(_f)
		_fl.close()

	def _readPxsFromFl(self, fl: str = "pydisp"):
		_fl = open(fl, "rb")
		_f = _fl.read()
		_fl.close()

		i = 0
		x = self.settings["resolutionX"]
		y = self.settings["resolutionY"]
		for b in _f:
			self._pxs[i%x][int(i/y)] = b

	def _fillArr(s: tuple[int, int]):
		arr = list[list[int]]()
		for y in range(s[0]):
			arr.append(list[int]())
			for x in range(s[1]):
				arr[y].append(0)
		return arr

	def new(self, resolution: tuple[int, int], scale: int = 5):
		self.settings = {
			"resolutionX": resolution[0],
			"resolutionY": resolution[1],
			"scale": scale
		}

		self.scr = display.set_mode((resolution[0] * scale, resolution[1] * scale))
		self._pxs = PyDisp._fillArr(resolution)
		self._savePxsToFl()

		display.set_caption(f"Matto's PyDisp v{_ver}")

		return self


	def drawRect(self, color: int, rect: tuple[int, int, int, int]):
		for y in range(rect[3]):
			for x in range(rect[2]):
				self.setPx(rect[0] + x, rect[1] + y, color)

	def wait(fps: int):
		display.update()
		Clock().tick(fps)
