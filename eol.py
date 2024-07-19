import pygame

class EOL:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.parent = pygame.display.get_surface()
		self.img = pygame.image.load("images/eol.png")
		self.rect = pygame.Rect(self.x, self.y, self.img.get_width(), self.img.get_height())

	def render(self):
		self.parent.blit(self.img, (self.x, self.y))