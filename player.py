import pygame

pygame.init()

class Player:
	def __init__(self, x, y, platforms):
		self.x = x
		self.y = y
		self.speed_y = 0
		self.speed_x = 0
		self.size = (32, 28)
		self.parent = pygame.display.get_surface()
		self.idle = pygame.transform.scale(pygame.image.load("images/player/idle.png"), self.size)
		self.jump = pygame.transform.scale(pygame.image.load("images/player/jump.png"), self.size)
		self.fall = pygame.transform.scale(pygame.image.load("images/player/fall.png"), self.size)
		self.current = self.idle
		self.left = False
		self.platforms = platforms
		self.rect = None
		self.jump_height = 8
		self.hspeed = 5
		self.resistance = 0.7
		self.falling = 0
		self.gravity = 0.5

	def render(self):
		self.parent.blit(self.current, (self.x, self.y))

		if self.falling < 3:
			self.current = self.idle
		else:
			if self.speed_y > 0:
				self.current = self.fall
			else:
				self.current = self.jump

		if self.left:
			self.current = pygame.transform.flip(self.current, 1, 0)

	def rect_update(self):
		self.rect = pygame.Rect(self.x+5, self.y, self.current.get_width()-10, self.current.get_height())

	def move_in_steps(self, steps):
		self.falling += 1
		for i in range(steps):
			last_value = self.x
			self.x += self.speed_x / steps
			self.rect_update()
			for p in self.platforms:
				if p.colliderect(self.rect):
					self.x = last_value
					self.rect_update()
					self.speed_x = 0

			last_value = self.y
			self.y += self.speed_y / steps
			self.rect_update()
			for p in self.platforms:
				if p.colliderect(self.rect):
					self.y = last_value
					self.rect_update()
					if self.speed_y > 0:
						self.falling = 0
					self.speed_y = 0

	def update(self):
		self.rect_update()

		# self.y += self.speed_y

		# for p in self.platforms:
		# 	if p.colliderect(self.rect):
		# 		self.fix_overlap(p)
		# 		self.speed_y = 0

		keys = pygame.key.get_pressed()

		if keys[pygame.K_UP] and self.falling < 5:
			self.speed_y = -self.jump_height

		if keys[pygame.K_RIGHT]:
			self.speed_x = self.hspeed
			self.left = False
		if keys[pygame.K_LEFT]:
			self.speed_x = -self.hspeed
			self.left = True

		self.speed_y += self.gravity
		self.speed_x = self.speed_x * self.resistance

		self.move_in_steps(round(abs(self.speed_y) + abs(self.speed_x)))