import pygame


class MyPlane(pygame.sprite.Sprite):
    def __init__(self, bg_size, screen):
        pygame.sprite.Sprite.__init__(self)  # 初始化飞机对象
        self.bg_size = bg_size
        self.screen = screen
        self.wd = False
        self.speed = 10
        self.width, self.height = bg_size[0], bg_size[1]
        # 飞机变换形态的图片
        # 使用convert（）方法能提高blit的切换速率，convert_alpha() 在原基础上增加了保留透明度
        self.plane_1 = pygame.image.load("image\\hero1.png").convert_alpha()
        self.plane_2 = pygame.image.load("image\\hero2.png").convert_alpha()
        self.getover_image_list = [pygame.image.load("image\\hero_blowup_n1.png").convert_alpha(),
                             pygame.image.load("image\\hero_blowup_n2.png").convert_alpha(),
                             pygame.image.load("image\\hero_blowup_n3.png").convert_alpha(),
                             pygame.image.load("image\\hero_blowup_n4.png").convert_alpha()]

        self.rect = self.plane_1.get_rect()  # 创建矩形对象
        self.mask = pygame.mask.from_surface(self.plane_1) # 去除图片的透明边框，便于更加准确的检测对象是否被碰撞
        # 初始化飞机出生地
        self.rect.left, self.rect.top = \
            (self.width - self.rect.w) // 2, \
            self.height - self.rect.h - 60

        # 设定飞机的移动范围
    def moveUP(self):
        if 0 < self.rect.top < self.height - 60:
            self.rect.top -= self.speed
        else:
            self.rect.top = 0

    def moveDOWN(self):
        if 0 < self.rect.bottom < self.height - 60:
            self.rect.top += self.speed
        else:
            self.rect.bottom = self.height - 60

    def moveLEFT(self):
        if 0 < self.rect.left < self.width:
            self.rect.left -= self.speed
        else:
            self.rect.left = 0

    def moveRIGHT(self):
        if 0 < self.rect.right < self.width:
            self.rect.left += self.speed
        else:
            self.rect.right = self.width

    def start_pos(self):
        self.wd = True
        self.rect.left, self.rect.top = \
            (self.width - self.rect.w) // 2, self.height - self.rect.h - 60


