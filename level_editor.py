import pygame
from pygame.locals import *
from spike import Spike
from eol import EOL
from dialog import Dialog

width, height = 1000, 630
display = pygame.display.set_mode((width, height))

pygame.display.set_caption("LManiks Level Editor")

mouse_init = False
tile_size = 32

mousex_init = 0
mousey_init = 0

platformw = 0
platformh = 0

platforms = []
platform_index = 0

dialogs = []

spikes = []
spike_index = 0
s = False

manik = False
manik_x = 0
manik_y = 0

eol_x = 0
eol_y = 0

clock = pygame.time.Clock()

def draw_grid():
	for i in range(round(width/tile_size)):
		pygame.draw.line(display, (100, 100, 100), (tile_size*i, 0), (tile_size*i, height))

	for i in range(round(height/tile_size)):
		pygame.draw.line(display, (100, 100, 100), (0, tile_size*i), (width, tile_size*i))

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
		if event.type == MOUSEBUTTONUP:
			mouse_init = False
		if event.type == KEYDOWN:
			if event.key == pygame.K_m:
				platforms.append(0)
				platforms[platform_index] = pygame.Rect(mousex_init, mousey_init, platformw, platformh)
				mouse_init = False

				mousex_init = 0
				mousey_init = 0

				platformw = 0
				platformh = 0
				platform_index += 1
			if event.key == pygame.K_n:
				s = True
			if event.key == pygame.K_l:
				try:
					platforms.remove(platforms[len(platforms)-1])
				except:
					print("no.")
			if event.key == pygame.K_k:
				try:
					spikes.remove(spikes[len(spikes)-1])
				except:
					print("no.")
			if event.key == pygame.K_s:
				level = open("levels/backup.py", "w")
				level.write("platforms = [\n")
				for platform in platforms:
					level.write(f"	pygame.Rect({platform.x}, {platform.y}, {platform.width}, {platform.height}),\n")
				level.write("]\n")
				level.write("spikes = [\n")
				for spike in spikes:
					level.write(f"	Spike({spike.x}, {spike.y}, False),\n")
				level.write("]\n")
				level.write(f"\nmanik_x = {manik_x}\nmanik_y = {manik_y}\nmanik=True\n")
			if event.key == pygame.K_a:
				file = open("levels/backup.py", "r")
				file_read = file.read()
				exec(file_read)
			if event.key == pygame.K_d:
				dialogs.append(Dialog(mousex, mousey, []))

	display.fill((255, 255, 255))

	# Mouse Setup
	mouse = pygame.mouse.get_pressed()[0]

	mousex = pygame.mouse.get_pos()[0] - (tile_size/2)
	mousey = pygame.mouse.get_pos()[1] - (tile_size/2)

	mousex = round(mousex / tile_size) * tile_size
	mousey = round(mousey / tile_size) * tile_size

	if mouse:
		if not mouse_init:
			mousex_init = mousex
			mousey_init = mousey
			mouse_init = True
		else:
			platformw = mousex - mousex_init
			platformh = mousey - mousey_init

	# Platforms
	print("platforms = [")
	for platform in platforms:
		w = round(platform.width / tile_size)
		h = round(platform.height / tile_size)
		img = pygame.image.load("images/tile2.png")
		imger = pygame.transform.scale(img, (tile_size, tile_size))
		for i in range(w):
			display.blit(imger, (platform.x+(i*tile_size), platform.y))
			for j in range(h):
				display.blit(imger, (platform.x+(i*tile_size), platform.y+(j*tile_size)))
		print(f"	pygame.Rect({platform.x}, {platform.y}, {platform.width}, {platform.height}),")
	print("]")

	# Spikes
	print("\nspikes = [")
	for spike in spikes:
		spike.render()
		print(f"	Spike({spike.x}, {spike.y}, False),")
	print("]\n")

	print ("\ndialogs = [")
	for dialog in dialogs:
		dialog.render()
		print(f"	Dialog({dialog.x}, {dialog.y}, []),")
	print("]\n")

	pygame.draw.rect(display, (0, 0, 0), (mousex_init, mousey_init, platformw, platformh))

	# EOL
	eol = EOL(eol_x, eol_y)
	eol.render()
	if pygame.key.get_pressed()[K_q]:
		eol_x = mousex
		eol_y = mousey
	print(f"eol_x = {eol_x}")
	print(f"eol_y = {eol_y}")

	# Manikom
	if not manik:
		if pygame.key.get_pressed()[K_b]:
			manik_x = mousex
			manik_y = mousey
			manik = True

	if manik:
		imgo = pygame.transform.scale(pygame.image.load("images/player/idle.png"), (tile_size, tile_size))
		display.blit(imgo, (manik_x, manik_y))
		if pygame.key.get_pressed()[K_v]:
			manik_x = mousex
			manik_y = mousey
		print(f"player_x = {manik_x}")
		print(f"player_y = {manik_y}")

	if s:
		spikes.append(Spike(mousex, mousey, True))
		s = False

	draw_grid()

	pygame.draw.rect(display, (255, 0, 0), (mousex, mousey, tile_size, tile_size), 2)

	pygame.display.update()
	clock.tick(60)
