import pygame

pygame.init()

class Dialog:
	def __init__(self, x, y, content):
		self.x = x
		self.y = y
		self.parent = pygame.display.get_surface()
		self.img = pygame.image.load("images/dialog.png")
		self.imgio = pygame.image.load("images/dialogio.png")
		self.rect = pygame.Rect(self.x, self.y, self.img.get_width(), self.img.get_height())
		self.content = content
		self.tooltip = False
		self.dia = False
		self.index = 0
		self.imageio = pygame.image.load("images/tile.png")

	def render(self):
		if self.tooltip:
			self.parent.blit(self.imgio, (self.x, self.y))
		else:
			self.parent.blit(self.img, (self.x, self.y))
	
	def update(self):
		k = pygame.key.get_pressed()
		if self.dia:
			x = 40
			y = 320
			w = 992 - (x * 2)
			h = 600 - (y + 20)
			pygame.draw.rect(self.parent, (5, 10, 20), (x, y-40, w, h+40))

			font = pygame.font.Font("pixelsans.ttf", 30)
			text_surf = font.render(self.content[self.index][1], True, (255, 255, 255))

			if self.content[self.index][0] == "Manikom":
				self.imageio = pygame.image.load("images/player/idle.png")
				self.imageio = pygame.transform.scale(self.imageio, (100, 80))
			if self.content[self.index][0] == "Romania":
				self.imageio = pygame.image.load("images/dialogs/romania.png")
				self.imageio = pygame.transform.scale(self.imageio, (100, 80))
				self.imageio = pygame.transform.flip(self.imageio, True, False)
			
			self.parent.blit(text_surf, (x, y))

			if self.content[self.index][0] == "Manikom":
				self.parent.blit(self.imageio, (x+40, y-70))
			else:
				self.parent.blit(self.imageio, (w-x-40, y-70))

			if k[pygame.K_ESCAPE]:
				self.dia = False
