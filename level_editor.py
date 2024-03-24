import pygame
from pygame.locals import *

width, height = 1000, 600
display = pygame.display.set_mode((width, height))

mouse_init = False
tile_size = 32

mousex_init = 0
mousey_init = 0

platformw = 0
platformh = 0

platforms = []
platform_index = 0

manikom = False
manik_x = 0
manik_y = 0

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

	display.fill((255, 255, 255))

	mouse = pygame.mouse.get_pressed()[0]

	mousex = pygame.mouse.get_pos()[0]
	mousey = pygame.mouse.get_pos()[1]

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

	print("level = [")
	for platform in platforms:
		pygame.draw.rect(display, (0, 0, 0), platform)
		print(f"	pygame.Rect({platform.x}, {platform.y}, {platform.width}, {platform.height}),")
	print("]")
	pygame.draw.rect(display, (0, 0, 0), (mousex_init, mousey_init, platformw, platformh))

	if not manik:
		if pygame.key.get_pressed()[K_n]:
			manik = True


	draw_grid()

	pygame.display.update()
	clock.tick(60)
