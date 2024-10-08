import pygame

pygame.init()

class Player:
        def __init__(self, x, y, platforms):
                self.x = x
                self.y = y
                self.prevcord = [self.x, self.y]
                self.speed_y = 0
                self.speed_x = 0
                self.parent = pygame.display.get_surface()
                self.idle = pygame.image.load("images/player/idle.png").convert_alpha()
                self.jump = pygame.image.load("images/player/jump.png").convert_alpha()
                self.fall = pygame.image.load("images/player/fall.png").convert_alpha()
                self.dashing = False
                self.current = self.idle
                self.left = False
                self.platforms = platforms
                self.rect = None
                self.jump_height = 8
                self.hspeed_normal = 5
                self.hspeed = 5
                self.resistance = 0.75
                self.falling = 0
                self.gravity = 0.45

        def rect_update(self):
                self.rect = pygame.Rect(self.x, self.y, self.idle.get_width(), self.idle.get_height())

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
                #       if p.colliderect(self.rect):
                #               self.fix_overlap(p)
                #               self.speed_y = 0

                keys = pygame.key.get_pressed()

                if keys[pygame.K_z] and self.falling < 5:
                        self.speed_y = -self.jump_height

                if keys[pygame.K_RIGHT]:
                        self.speed_x = self.hspeed
                        self.left = False
                if keys[pygame.K_LEFT]:
                        self.speed_x = -self.hspeed
                        self.left = True
                
                if keys[pygame.K_x]:
                        self.hspeed = 15
                        self.dashing = True
                else:
                        self.hspeed = self.hspeed_normal
                        self.dashing = False

                self.speed_y += self.gravity
                self.speed_x = self.speed_x * self.resistance

                if self.x < 0:
                        self.x = 0
                if self.x > 928:
                        self.x = 928

                self.move_in_steps(round(abs(self.speed_y) + abs(self.speed_x)))
                q = pygame.image.load("images/player/idle.png")
                q.set_alpha(100)
                self.parent.blit(q, self.prevcord)
                self.prevcord = [self.x, self.y]
        
        def render(self):
                if self.left:
                        self.current = pygame.transform.flip(self.current, 1, 0)
                
                self.parent.blit(self.current, (self.x, self.y))

                if self.falling < 3:
                        self.current = self.idle
                else:
                        if self.speed_y > 0:
                                self.current = self.fall
                        else:
                                self.current = self.jump
