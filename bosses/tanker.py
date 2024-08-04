import pygame, math

class Tanker:
	def __init__(self, x, y):
		self.numero = 450
		self.x = x + self.numero
		self.y = y
		self.parent = pygame.display.get_surface()
		self.img = pygame.image.load("images/bosses/tanker.png").convert_alpha()
		self.imgo = pygame.image.load("images/bosses/tanker_fill.png").convert_alpha()
		self.imgn = pygame.image.load("images/bosses/tanker.png").convert_alpha()
		self.rect = pygame.Rect(self.x, self.y, self.img.get_width(), self.img.get_height())
		self.hp = 120
		self.full_hp = 120
		self.e = 4
		self.f = self.numero
		self.acc = 5
		self.intro = True

	def render(self):
		# self.x += math.cos(self.o / 32)
		self.parent.blit(self.img, (self.x, self.y))
	
	def rect_update(self):
		self.rect = pygame.Rect(self.x, self.y, self.img.get_width(), self.img.get_height())
	
	def update(self):
		self.rect = pygame.Rect(self.x, self.y, self.img.get_width(), self.img.get_height())
		if not self.intro:
			self.e += 1
			self.f -= 1
			if self.e < 1:
				self.img = self.imgo
			else:
				self.img = self.imgn
			if self.acc < 1:
				self.x -= self.acc
				self.acc += 1
		else:
			self.f -= self.acc
			self.x -= self.acc
			self.acc += 0.5
			if self.f < 1:
				self.f = 0
				self.acc = -10
				self.intro = False
