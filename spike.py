import pygame

class Spike:
	def __init__(self, x, y, tvoyo, tile_size=32):
		self.x = x
		self.y = y
		self.parent = pygame.display.get_surface()
		self.img = pygame.image.load("images/spike3.png")
		if tvoyo:
			self.x = self.x + (tile_size - self.img.get_width())
			self.y = self.y + (tile_size - self.img.get_height())
		tvoyox = 8
		tvoyoy = 10
		self.rect = pygame.Rect(self.x+tvoyox, self.y+tvoyoy, self.img.get_width()-(tvoyox * 2), self.img.get_height()-(tvoyoy * 2))

	def render(self, tile_size=32):
		self.parent.blit(self.img, (self.x, self.y))

class Thing:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.parent = pygame.display.get_surface()
		self.img = pygame.image.load("images/tile.png")
		self.rect = pygame.Rect(self.x, self.y, self.img.get_width(), self.img.get_height())

	def render(self):
		self.parent.blit(self.img, (self.x, self.y))
		pygame.draw.rect(self.parent, (0, 0, 0), self.rect)