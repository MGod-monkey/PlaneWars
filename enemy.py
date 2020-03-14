import pygame
from random import *


class SmallEnemy(pygame.sprite.Sprite):
    def __init__(self, screen_size, mode_s, screen):
        pygame.sprite.Sprite.__init__(self)  # 小号敌人
        self.screen_size = screen_size
        self.screen = screen
        self.hp = 1
        self.s_speed = int(mode_s[0])
        self.width, self.height = self.screen_size[0], self.screen_size[1]
        self.s_start = - int(mode_s[1]) * self.height
        self.s_end = - int(mode_s[2]) * self.height

        self.s_enemy_image = pygame.image.load("image\\enemy0.png").convert_alpha()
        self.getover_image_list = [pygame.image.load("image\\enemy0_down1.png").convert_alpha(),
                                   pygame.image.load("image\\enemy0_down1.png").convert_alpha(),
                                   pygame.image.load("image\\enemy0_down3.png").convert_alpha(),
                                   pygame.image.load("image\\enemy0_down4.png").convert_alpha()]

        self.rect = self.s_enemy_image.get_rect()
        self.mask = pygame.mask.from_surface(self.s_enemy_image)
        self.rect.left, self.rect.top = randint(0, self.width - self.rect.width), \
                                        randint(self.s_start, self.s_end)

        # 设置小号敌人出生地

    def start_pos(self):
        self.hp = 1
        self.rect.left, self.rect.top = randint(0, self.width - self.rect.width), \
                                        randint(self.s_start, self.s_end)

    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.s_speed
        else:
            self.start_pos()

    def appear(self):
        self.screen.blit(self.s_enemy_image, self.rect)


class MidEnemy(pygame.sprite.Sprite):
    def __init__(self, screen_size, mode_m, screen):
        pygame.sprite.Sprite.__init__(self)  # 中号敌人
        self.screen_size = screen_size
        self.hp = 5
        self.hit = False
        self.screen = screen
        self.m_speed = int(mode_m[0])
        self.width, self.height = self.screen_size[0], self.screen_size[1]
        self.m_start = - int(mode_m[1]) * self.height
        self.m_end = - int(mode_m[2]) * self.height

        self.m_enemy_image_1 = pygame.image.load("image\\enemy1.png").convert_alpha()
        self.m_enemy_image_2 = pygame.image.load("image\\enemy1_hit.png").convert_alpha()
        self.getover_image_list = [pygame.image.load("image\\enemy1_down1.png").convert_alpha(),
                                   pygame.image.load("image\\enemy1_down1.png").convert_alpha(),
                                   pygame.image.load("image\\enemy1_down3.png").convert_alpha(),
                                   pygame.image.load("image\\enemy1_down4.png").convert_alpha()]

        self.rect = self.m_enemy_image_1.get_rect()
        self.mask = pygame.mask.from_surface(self.m_enemy_image_1)
        self.rect.left, self.rect.top = randint(0, self.width - self.rect.width), \
                                        randint(self.m_start, self.m_end)

        # 设置中号敌人出生地

    def start_pos(self):
        self.hp = 5
        self.rect.left, self.rect.top = randint(0, self.width - self.rect.width), \
                                        randint(self.m_start, self.m_end)

    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.m_speed
        else:
            self.start_pos()

    def appear(self):
        self.screen.blit(self.m_enemy_image_1, self.rect)

    def get_hit(self):
        self.screen.blit(self.m_enemy_image_2, self.rect)


class BigEnemy(pygame.sprite.Sprite):
    def __init__(self, screen_size, mode_b, screen):
        pygame.sprite.Sprite.__init__(self)
        self.screen_size = screen_size
        self.screen = screen
        self.active = True
        self.hit = False
        self.hp = 15
        self.b_speed = int(mode_b[0])
        self.width, self.height = self.screen_size[0], self.screen_size[1]
        self.b_start = - int(mode_b[1]) * self.height
        self.b_end = - int(mode_b[2]) * self.height

        self.b_enemy_image_1 = pygame.image.load("image\\enemy2.png").convert_alpha()
        self.b_enemy_image_2 = pygame.image.load("image\\enemy2_n2.png").convert_alpha()
        self.b_enemy_image_3 = pygame.image.load("image\\enemy2_hit.png").convert_alpha()
        self.getover_image_list = [pygame.image.load("image\\enemy2_down1.png").convert_alpha(),
                                   pygame.image.load("image\\enemy2_down2.png").convert_alpha(),
                                   pygame.image.load("image\\enemy2_down3.png").convert_alpha(),
                                   pygame.image.load("image\\enemy2_down4.png").convert_alpha(),
                                   pygame.image.load("image\\enemy2_down5.png").convert_alpha(),
                                   pygame.image.load("image\\enemy2_down6.png").convert_alpha()]

        self.rect = self.b_enemy_image_1.get_rect()
        self.mask = pygame.mask.from_surface(self.b_enemy_image_1)
        self.rect.left, self.rect.top = randint(0, self.width - self.rect.width), \
                                        randint(self.b_start, self.b_end)

        # 设置大号敌人出生地

    def start_pos(self):
        self.hp = 15
        self.rect.left, self.rect.top = randint(0, self.width - self.rect.width), \
                                        randint(self.b_start, self.b_end)

    def move(self):
        if self.rect.top < self.height + self.rect.width:
            self.rect.top += self.b_speed
        else:
            self.start_pos()

    def switchimage1(self):
        self.screen.blit(self.b_enemy_image_1, self.rect)

    def switchimage2(self):
        self.screen.blit(self.b_enemy_image_2, self.rect)

    def get_hit(self):
        self.screen.blit(self.b_enemy_image_3, self.rect)
