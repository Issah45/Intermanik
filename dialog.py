import pygame

pygame.init()

class Dialog:
	def __init__(self, x, y, content, imger="images/dialog.png", imgerflip=False):
		self.x = x
		self.y = y
		self.parent = pygame.display.get_surface()
		self.img = pygame.image.load(imger)
		if imgerflip:
			self.img = pygame.transform.flip(self.img, True, False)
		self.imganim = 0
		self.maximganim = 15
		self.rect = pygame.Rect(self.x, self.y, self.img.get_width(), self.img.get_height())
		self.omg = pygame.image.load("images/dialogs/tooltip.png")
		self.content = content
		self.tooltip = False
		self.dia = False
		self.previndex = 0
		self.index = 0
		# self.imageio = pygame.image.load("images/tile.png")

	def render(self):
		self.parent.blit(self.img, (self.x, self.y))
		if self.tooltip:
			self.parent.blit(self.omg, (self.x, self.y-25))
	
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

			contentio = self.content[self.index][0].lower()
			self.imageio = pygame.image.load(f"images/dialogs/{contentio}.png")
			self.imageio = pygame.transform.scale(self.imageio, (100, 80))
			
			self.parent.blit(text_surf, (x, y))

			if contentio == "manikom" or contentio == "manikom_bored" or contentio == "manikom_confused":
				_x = x+40
				_y = y - 80
			else:
				self.imageio = pygame.transform.flip(self.imageio, True, False)
				_x = w-x-40
				_y = y-80
			
			if self.imganim == self.maximganim:
				_y = _y - self.maximganim
			if self.imganim > 0:
				_y = _y + self.imganim

			self.parent.blit(self.imageio, (_x, _y))

			# Animation
			self.imganim -= 1
			
			if self.index != self.previndex:
				self.imganim = self.maximganim
				self.previndex = self.index

			if k[pygame.K_ESCAPE]:
				self.dia = False
