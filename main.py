import pygame, os
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

# Mouse
mouse_rect = pygame.Rect(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], 20, 20)

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
    display.fill((30, 50, 80))

    display.blit(playbutton_img, (playbutton_x, playbutton_y))
    pygame.draw.rect(display, (0, 0, 0), mouse_rect)

    mouse_rect = pygame.Rect(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], 20, 20)

    if mouse_rect.colliderect(playbutton_rect) and pygame.mouse.get_pressed()[0]:
        break

    pygame.display.update()
    clock.tick(60)

os.system("python game.py")