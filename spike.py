import pygame

class Spike:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.parent = pygame.display.get_surface()
		self.img = pygame.image.load("images/spike2.png")
		v = 5
		self.rect = pygame.Rect(self.x+v, self.y+v, self.img.get_width()-(v*2), self.img.get_height()-(2*v))

	def render(self):
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