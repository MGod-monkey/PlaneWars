import pygame
from random import randint


class BulletSupply(pygame.sprite.Sprite):
    def __init__(self, screen, screen_size):
        pygame.sprite.Sprite.__init__(self)
        self.active = False
        self.screen = screen
        self.width, self.height = screen_size[0], screen_size[1]
        self.speed = 5
        self.bullet_image = pygame.image.load("image\\bullet_supply.png").convert_alpha()
        self.rect = self.bullet_image.get_rect()
        self.mask = pygame.mask.from_surface(self.bullet_image)

    def start_pos(self):
        self.rect.left, self.rect.top = randint(0, self.width - self.rect.width) ,\
                                        randint(-100, 0)

    def move(self):
        self.rect.top += self.speed
        if self.rect.top > self.height:
            self.active = False

    def appear(self):
        self.screen.blit(self.bullet_image, self.rect)


class BombSupply(pygame.sprite.Sprite):
    def __init__(self, screen, screen_size):
        pygame.sprite.Sprite.__init__(self)
        self.active = False
        self.screen = screen
        self.width, self.height = screen_size[0], screen_size[1]
        self.speed = 5
        self.bomb_image = pygame.image.load("image\\bomb_supply.png").convert_alpha()
        self.rect = self.bomb_image.get_rect()
        self.mask = pygame.mask.from_surface(self.bomb_image)

    def start_pos(self):
        self.rect.left, self.rect.top = randint(0, self.width - self.rect.width) ,\
                                        randint(-100, -80)

    def move(self):
        self.rect.top += self.speed
        if self.rect.top > self.height:
            self.active = False

    def appear(self):
        self.screen.blit(self.bomb_image, self.rect)