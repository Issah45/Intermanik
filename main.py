import pygame, os, math
from pygame.locals import *

width, height = 992, 600
display = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

# Play Button
playbutton_img = pygame.image.load("images/playbtn.png")
playbutton_x = round(width / 2) - (playbutton_img.get_width() / 2)
playbutton_y = round(height / 1.25) - (playbutton_img.get_height() / 2)
playbutton_rect = pygame.Rect(playbutton_x, playbutton_y,
                  playbutton_img.get_width(), playbutton_img.get_height())

# Title
title_img = pygame.image.load("images/title.png")
title_x = round(width / 2) - (title_img.get_width() / 2)
title_y = round(height / 3.5) - (title_img.get_height() / 2)
o = 0

# Mouse
mouse_rect = pygame.Rect(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], 20, 20)

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
    display.fill((10, 20, 30))

    display.blit(playbutton_img, (playbutton_x, playbutton_y))
    display.blit(title_img, (title_x, title_y))

    title_y += math.sin(o)
    o += 0.1

    playbutton_y += math.cos(o)

    mouse_rect = pygame.Rect(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], 20, 20)

    if mouse_rect.colliderect(playbutton_rect) and pygame.mouse.get_pressed()[0]:
        break

    pygame.display.update()
    clock.tick(60)

try:
    os.system("python game.py")
except:
    os.system("python3 game.py")