import pygame

class Spike:
	def __init__(self, x, y, tile_size=32):
		self.x = x
		self.y = y
		self.parent = pygame.display.get_surface()
		self.img = pygame.image.load("images/spike3.png")
		self.x = self.x + (tile_size - self.img.get_width())
		self.y = self.y + (tile_size - self.img.get_height())
		self.rect = pygame.Rect(self.x, self.y, self.img.get_width(), self.img.get_height())

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