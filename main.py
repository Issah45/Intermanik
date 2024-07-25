import pygame
from pygame.locals import *

# Imports
from player import Player
from dialog import Dialog
from spike import Spike
from eol import EOL

# Setup
width, height = 992, 600
display = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
tile_size = 32
level = 1

bgm = pygame.mixer.Sound("sounds/intermanik.wav")
bgm.play()

pygame.display.set_caption("LManiks")

# Functions
def approx(a):
	a = round(a/tile_size) * tile_size

# Variables & O
player_x, player_y = 0, 0
platforms, spikes = [], []
exec(open(f"levels/level{level}.py").read())
eol = EOL(eol_x, eol_y)
player = Player(player_x, player_y, platforms)

# Game Loop
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
	display.fill((50, 150, 250))

	# Platforms
	for platform in platforms:
		w = round(platform.width / tile_size)
		h = round(platform.height / tile_size)
		img = pygame.image.load("images/tile4.png")
		imger = pygame.transform.scale(img, (tile_size, tile_size))
		for i in range(w):
			display.blit(imger, (platform.x+(i*tile_size), platform.y))
			for j in range(h):
				display.blit(imger, (platform.x+(i*tile_size), platform.y+(j*tile_size)))

	# Updates
	player.update()

	# Renders
	player.render()
	eol.render()

	# Collisions
	for spike in spikes:
		spike.render()
		# print(spike.rect)
		if spike.rect.colliderect(player.rect):
			pygame.quit()
	
	if player.rect.colliderect(eol.rect):
		level += 1
		exec(open(f"levels/level{level}.py").read())
		eol = EOL(eol_x, eol_y)
		player = Player(player_x, player_y, platforms)

	pygame.display.update()
	clock.tick(60)