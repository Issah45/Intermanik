import pygame, math

class LavaBall:
    def __init__(self, x, y, spd=0.06):
        self.x = x
        self.y = y
        self.orgX = x
        self.orgY = y
        self.z = 0
        self.dist = 4
        self.spd = spd
        self.parent = pygame.display.get_surface()
        self.img = pygame.image.load("images/bosses/tanker_bullet.png")
        self.rect = pygame.Rect(self.x, self.y, self.img.get_width(), self.img.get_height())
    
    def rect_update(self):
        self.rect = pygame.Rect(self.x, self.y, self.img.get_width(), self.img.get_height())

    def render(self):
        self.parent.blit(self.img, (self.x, self.y))
        # pygame.draw.rect(self.parent, (0, 0, 0), self.rect)
    
    def update(self):
        self.rect_update()
        self.x += math.cos(self.z) * self.dist
        self.y += math.sin(self.z) * self.dist
        self.z += self.spd