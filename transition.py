
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