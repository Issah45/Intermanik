import pygame, math

class TankerThug:
	def __init__(self, x, y, dir):
		self.x = x
		self.y = y
		self.parent = pygame.display.get_surface()
		self.img = pygame.image.load("images/bosses/tanker_thug.png")
		self.rect = pygame.Rect(self.x, self.y, self.img.get_width(), self.img.get_height())
		self.dir = dir
		self.o = False

	def render(self):
		self.parent.blit(self.img, (self.x, self.y))
	
	def rect_update(self):
		self.rect = pygame.Rect(self.x, self.y, self.img.get_width(), self.img.get_height())
	
	def update(self):
		self.x -= math.sin(self.dir) * 4
		self.y -= math.cos(self.dir) * 4
		self.rect_update()