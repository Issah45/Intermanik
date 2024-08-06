import pygame
from pygame.locals import *

# Imports
from random import randint as rand
from player import Player
from dialog import Dialog
from spike import Spike
from eol import EOL
from dialog import Dialog
from lavaball import LavaBall
from bosses.tanker import Tanker
from bosses.tanker_bullet import TankerBullet
from bosses.tanker_thug import TankerThug
pygame.init()

# Setup
width, height = 960, 600
display = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
tile_size = 32
level = int(open("levelsave", "r").read())
bossmode = 0
_bossmode = False
holdinger = False
screen_shake = 0
max_screen_shake = 100
blocks = 0
block_lim = 3

# Tanker Init
tanker = Tanker(592, 378)
tanker_bullets = []
tanker_delay = 20
tanker_thugs = []
tankershot = False

# Transition
transition = 0
trans = pygame.Surface((width, height))
trans.set_alpha(transition)
trans.fill((255,255,255))

bg = pygame.transform.scale(pygame.image.load("images/sky.jpg"), (width, height)).convert()
bg2 = pygame.transform.scale(pygame.image.load("images/cave.jpg"), (width, height)).convert()

pygame.display.set_caption("LManiks")

# Functions
def approx(a):
	a = round(a/tile_size) * tile_size

def restart():
	# platforms = []
	eol = EOL(eol_x, eol_y)
	player.x = player_x
	player.y = player_y
	player.rect_update()

def round32(what):
	return round(what/32) * 32

# Variables & O
player_x, player_y = 0, 0
platforms, spikes, dialogs, lavaballs = [], [], [], []
exec(open(f"levels/level{level}.py").read())
eol = EOL(eol_x, eol_y)
player = Player(player_x, player_y, platforms)

qua = pygame.Surface((50, 50))

# Game Loop
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
		if event.type == KEYDOWN:
			if event.key == K_c and blocks < block_lim:
				if player.left: x = round32(player.x) - 32
				else: x = round32(player.x) + 32
				y = round32(player.y)

				r = pygame.Rect(x, y, 32, 32)

				if player.rect.colliderect(r):
					if player.left: x -= 32
					else: x += 32
					r = pygame.Rect(x, y, 32, 32)
				blocks += 1

				platforms.append(r)
			if event.key == K_r:
				exec(open(f"levels/level{level}.py").read())
				restart()
				player.platforms = platforms
				screen_shake = 100
				blocks = 0
	display.fill((50, 150, 250))
	# Background
	if level <= 9:
		display.blit(bg, (0, 0))
	if level == 9:
		display.blit(bg2, (round(width*2/3), 0))
	# Platforms
	for platform in platforms:
		w = round(platform.width / tile_size)
		h = round(platform.height / tile_size)
		img = pygame.image.load("images/tile4.png").convert()
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

	# Bounds
	if player.y > 650:
		exec(open(f"levels/level{level}.py").read())
		restart()
		player.platforms = platforms
		screen_shake = 100
		blocks = 0

	# Collisions & Stuff
	for spike in spikes:
		spike.render()
		if spike.rect.colliderect(player.rect):
			exec(open(f"levels/level{level}.py").read())
			restart()
			player.platforms = platforms
			screen_shake = 100
			blocks = 0
	
	if player.rect.colliderect(eol.rect):
		level += 1
		exec(open(f"levels/level{level}.py").read())
		eol = EOL(eol_x, eol_y)
		player = Player(player_x, player_y, platforms)
		transition = 255
		blocks = 0
		open("levelsave", "w").write(str(level))
	
	for lavaball in lavaballs:
		lavaball.render()
		lavaball.update()
		if player.rect and player.rect.colliderect(lavaball.rect):
			exec(open(f"levels/level{level}.py").read())
			restart()
			player.platforms = platforms
			screen_shake = 100
			blocks = 0

	# Dialog
	for dialog in dialogs:
		dialog.render()
		dialog.update()
		try: dialog.rect.colliderect(player.rect)
		except: pass
		else:
			if dialog.rect.colliderect(player.rect):
				dialog.tooltip = True
			else:
				dialog.tooltip = False
			
			if dialog.rect.colliderect(player.rect) and pygame.key.get_pressed()[K_x]:
				dialog.dia = True
			
			if dialog.dia and pygame.key.get_pressed()[K_DOWN] and not holdinger:
				dialog.index += 1
			if dialog.dia and pygame.key.get_pressed()[K_UP] and not holdinger:
				dialog.index -= 1
			if dialog.index >= len(dialog.content):
				dialog.dia = False
				dialog.index = 0
			if dialog.index < 0:
				dialog.index = 0
			
			if pygame.key.get_pressed()[K_UP] or pygame.key.get_pressed()[K_DOWN]:
				holdinger = True
			else:
				holdinger = False

	# Tanker
	if level == 8 and tanker.hp > 0:
		bossmode = 1
	if bossmode == 1:
		if tanker.hp < 1:
			bossmode = 0
			eol.x = 832
			eol.y = 512
			eol.rect_update()
		
		if tanker_delay < 1 and tanker.f < -100:
			tanker_bullets.append(TankerBullet(tanker.x+200, tanker.y+100, rand(0, 180)))
			tanker_thugs.append(TankerThug(tanker.x+200, tanker.y+100, rand(0, 180)))
			tanker_delay = 4
		
		for tanker_bullet in tanker_bullets:
			tanker_bullet.render()
			tanker_bullet.update()
			if player.rect.colliderect(tanker_bullet.rect):
				exec(open(f"levels/level{level}.py").read())
				restart()
				player.platforms = platforms
				screen_shake = 100
				tanker.hp = tanker.full_hp
				blocks = 0
		
		for tanker_thug in tanker_thugs:
			tanker_thug.render()
			tanker_thug.update()
			
			if player.rect.colliderect(tanker_thug.rect) and player.dashing and not tanker_thug.o:
				tanker_thug.dir = -tanker_thug.dir
				tanker_thug.o = True
				player.speed_x = -10
			
			if tanker.rect.colliderect(tanker_thug.rect) and tanker_thug.o:
				tanker.e = -5
				tanker.hp -= 8
				tanker_thugs.remove(tanker_thug)
		tanker.render()
		tanker.update()
		tanker_delay -= 1

		tankw = tanker.img.get_width() - 5
		pygame.draw.rect(display, (255, 0, 0), (tanker.x, tanker.y-20, tankw, 20))
		pygame.draw.rect(display, (0, 255, 100), (tanker.x, tanker.y-20, tankw * (tanker.hp / tanker.full_hp), 20))

	trans.set_alpha(transition)
	display.blit(trans, (0, 0))
	transition -= 20

	if screen_shake > 0:
		rand_value_x = rand(-10, 10) * (screen_shake / max_screen_shake)
		rand_value_y = rand(-10, 10) * (screen_shake / max_screen_shake)
		qua = pygame.transform.scale(display, (width, height)).convert()
		display.blit(qua, (rand_value_x, rand_value_y))
		screen_shake -= 1.25
	
	pygame.display.update()
	clock.tick(60)
