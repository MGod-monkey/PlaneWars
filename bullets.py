import pygame

class Bullet_1(pygame.sprite.Sprite):
    def __init__(self, postion):
        pygame.sprite.Sprite.__init__(self)
        self.bullet_image = pygame.image.load("image\\bullet.png")
        self.rect = self.bullet_image.get_rect()
        self.mask = pygame.sprite.from_surface(self.bullet_image)
        self.rect.left, self.rect.top = tuple(postion)
        self.speed = 12
        self.active = False

    def move(self):
        self.rect.top -= self.speed
        if self.rect.top < 0:
            self.active = False

    def start_pos(self, postion):
        self.active = True
        self.rect.left, self.rect.top = tuple(postion)


class Bullet_2(pygame.sprite.Sprite):
    def __init__(self, postion):
        pygame.sprite.Sprite.__init__(self)
        self.bullet_image = pygame.image.load("image\\bullet2.png").convert_alpha()
        self.mask = pygame.sprite.from_surface(self.bullet_image)
        self.speed = 15
        self.active = False
        self.rect = self.bullet_image.get_rect()
        self.rect.left, self.rect.top = postion

    def start_pos(self, postion):
        self.active = True
        self.rect.left, self.rect.top = postion

    def move(self):
        self.rect.top -= self.speed
        if self.rect.top < 0:
            self.active = False
