import pygame
from pygame.locals import *

from player import Player

width, height = 1000, 600
display = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
tile_size = 32

platforms = [
	pygame.Rect(64, 32, 96, 544),
	pygame.Rect(96, 512, 832, 64),
	pygame.Rect(224, 448, 128, 32),
	pygame.Rect(768, 160, 160, 32),
	pygame.Rect(608, 416, 64, 64),
	pygame.Rect(704, 384, 64, 64),
	pygame.Rect(800, 320, 64, 64),
	pygame.Rect(672, 192, 64, 64)
]
player = Player((1000/2)-150, 600/2, platforms)

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
	display.fill((50, 150, 250))

	for platform in platforms:
		w = round(platform.width / tile_size)
		h = round(platform.height / tile_size)
		img = pygame.image.load("images/tile2.png")
		imger = pygame.transform.scale(img, (tile_size, tile_size))
		for i in range(w):
			display.blit(imger, (platform.x+(i*tile_size), platform.y))
			for j in range(h):
				display.blit(imger, (platform.x+(i*tile_size), platform.y+(j*tile_size)))
		# pygame.draw.rect(display, (0, 0, 0), platform)

	# Renders
	player.render()

	# Updates
	player.update()

	pygame.display.update()
	clock.tick(60)