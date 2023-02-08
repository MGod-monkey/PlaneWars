import pygame
from sys import exit
from configparser import ConfigParser
from pygame.locals import *
from random import choice
from PlaneWars_Class import supply
from PlaneWars_Class import bullets
from PlaneWars_Class import enemy
from PlaneWars_Class import myplane

pygame.init()   # 屏幕初始化
pygame.mixer.init()  # 声音初始化
pygame.font.init()  # 字体初始化
config = ConfigParser()   # 配置信息初始化
font = pygame.font.Font("font\\Marker Felt.ttf", 36)   # 字体1对象初始化
font_2 = pygame.font.Font("font\\Marker Felt.ttf", 80)  # 字体2对象初始化
font_3 = pygame.font.Font("font\\字魂50号-白鸽天行体.ttf", 30)   # 字体3对象初始化
clock = pygame.time.Clock()  # 锁帧对象初始化


# 读取配置信息
config.read("config.ini")
screen_1_size = width_1, heigth_1 = config["display"].getint("size_1_w"),\
    config["display"].getint("size_1_h")
screen_2_size = width_2, heigth_2 = config["display"].getint("size_2_w"), \
    config["display"].getint("size_2_h")
volume = config["music"].getfloat("volume")
volume_2 = config["music"].getfloat("volume_2")
fps = config["display"].getint("fps")
delay = config["display"].getint("delay")
mode = eval(config["mode"].get("easy"))
last_bomb = config["supply"].getint("bomb_init_number")
double_bullet_time = config["supply"].getint("double_bullet_time")
mode_s, mode_m, mode_b, enemy_numbers = mode[0], mode[1], mode[2], mode[3]

# 窗口初始化
screen = pygame.display.set_mode(screen_1_size)
icon = pygame.image.load("image\\icon.png")
pygame.display.set_icon(icon)


# 载入音效
# 游戏开始页面音效
start_music = pygame.mixer.Sound("sound\\BGM_long.wav")
start_music.set_volume(volume)
# 游戏背景音乐
pygame.mixer.music.load("sound\\BGM.wav")
pygame.mixer.music.set_volume(volume_2)  # 音乐的音量设定，值在0到1
# 玩家死亡音效
user_getover = pygame.mixer.Sound("sound\\game_over.wav")
user_getover.set_volume(volume)
# 玩家获取炸弹道具音效
get_bomb_sound = pygame.mixer.Sound("sound\\get_bomb.wav")
get_bomb_sound.set_volume(volume)
# 玩家获取双倍炸弹音效
get_double_sound = pygame.mixer.Sound("sound\\get_double_laser.wav")
get_double_sound.set_volume(volume)
# 玩家开枪音效
bullet_sound = pygame.mixer.Sound("sound\\bullet.wav")
bullet_sound.set_volume(volume)
# 玩家中弹音效
get_bullet_sound = pygame.mixer.Sound("sound\\out_porp.wav")
get_bullet_sound.set_volume(volume)
# 按钮音效
button_sound = pygame.mixer.Sound("sound\\button.wav")
button_sound.set_volume(volume)
# 小型飞机毁灭音效
enemy0_down_sound = pygame.mixer.Sound("sound\\enemy0_down.wav")
enemy0_down_sound.set_volume(volume)
# 中型飞机毁灭音效
enemy1_down_sound = pygame.mixer.Sound("sound\\enemy1_down.wav")
enemy1_down_sound.set_volume(volume)
# 大型飞机毁灭音效
enemy2_down_sound = pygame.mixer.Sound("sound\\enemy2_down.wav")
enemy2_down_sound.set_volume(volume)
# 大型飞机出场音效
enemy2_appear_sound = pygame.mixer.Sound("sound\\big_plane_flying.wav")
enemy2_appear_sound.set_volume(volume)
# 使用全局炸弹音效
use_bomb_sound = pygame.mixer.Sound("sound\\use_bomb.wav")
use_bomb_sound.set_volume(volume)
# 圈住你
qzn_sound = pygame.mixer.Sound("sound\\圈住你-一口甜.wav")
qzn_sound.set_volume(volume)
# 无名之辈
wmzb_sound = pygame.mixer.Sound("sound\\无名之辈-陈雪燃.wav")
wmzb_sound.set_volume(volume)


# 载入图片
start_bg_image = pygame.image.load("image\\bg.png").convert()
action_image = pygame.image.load("image\\action.png").convert()
name_image = pygame.image.load("image\\name.png").convert_alpha()
bg_image = pygame.image.load("image\\background.png").convert()
life_image = pygame.image.load("image\\plane.png").convert_alpha()
get_over_image = pygame.image.load("image\\gameover.png").convert()
paused_nor_image = pygame.image.load("image\\game_pause_nor.png").convert_alpha()
paused_pressed_image = pygame.image.load("image\\game_pause_pressed.png").convert_alpha()
resume_nor_image = pygame.image.load("image\\game_resume_nor.png").convert_alpha()
resume_pressed_image = pygame.image.load("image\\game_resume_pressed.png").convert_alpha()
bomb_image = pygame.image.load("image\\bomb.png").convert_alpha()
button_not_image = pygame.image.load("image\\button_nor.png").convert_alpha()
button_pressed_image = pygame.image.load("image\\button_p.png").convert_alpha()
resume_font_image = pygame.image.load("image\\resume_nor.png").convert_alpha()
restart_font_image = pygame.image.load("image\\restart_nor.png").convert_alpha()
quit_font_image = pygame.image.load("image\\quit_nor.png").convert_alpha()
setting_nor_image = pygame.image.load("image\\setting.png").convert_alpha()
setting_pressed_image = pygame.image.load("image\\setting_pressed.png").convert_alpha()
music_play_image = pygame.image.load("image\\music.png").convert_alpha()
music_play_image2 = pygame.image.load("image\\music_pressed.png").convert_alpha()
music_stop_image2 = pygame.image.load("image\\music_stop_pressed.png").convert_alpha()
music_stop_image = pygame.image.load("image\\music_stop.png").convert_alpha()
author_nor_image = pygame.image.load("image\\author.png").convert_alpha()
author_pressed_image = pygame.image.load("image\\author_pressed.png").convert_alpha()
author_tx = pygame.image.load("image\\tx.png").convert_alpha()
author_bf = pygame.image.load("image\\author_bg.png").convert()
volume_image = pygame.image.load("image\\volume.png").convert_alpha()
volume_pole = pygame.image.load("image\\volume_pole.png").convert_alpha()
loading_image = [pygame.image.load("image\\game_loading1.png").convert_alpha(),
                 pygame.image.load("image\\game_loading2.png").convert_alpha(),
                 pygame.image.load("image\\game_loading3.png").convert_alpha(),
                 pygame.image.load("image\\game_loading4.png").convert_alpha()]


# 添加敌人飞机模块组
"""

   :param self_group: 个体组
   :param group: 公共组
   :param numbers: 生成的数量
   :return: None
   """
def add_small_enemies(self_group, group, numbers):
    for n in range(numbers):
        small_enemy = enemy.SmallEnemy(screen_2_size, mode_s, screen)
        self_group.add(small_enemy)
        group.add(small_enemy)
def add_mid_enemies(self_group, group, numbers):
    for n in range(numbers):
        small_enemy = enemy.MidEnemy(screen_2_size, mode_m, screen)
        self_group.add(small_enemy)
        group.add(small_enemy)
def add_big_enemies(self_group, group, numbers):
    for n in range(numbers):
        small_enemy = enemy.BigEnemy(screen_2_size, mode_b, screen)
        self_group.add(small_enemy)
        group.add(small_enemy)


# 写入历史最高纪录
def set_history_score(score, history_score):
    """

    :param score: 当前得分
    :param history_score: 历史最高分
    :return: 当前得分是否大于历史得分
    """
    if score > history_score:
        config.set("score", "history_score", str(score))
        config.write(open('config.ini', "r+"))
        return True
    return False


# 载入游戏动画
def display_loading(index, delay):
    loading_rect = loading_image[0].get_rect()
    while True:
        if not (delay % 5):
            if index == 0:
                loading_rect.left, loading_rect.top = width_1 // 2 - 80, 300
                name_image_rect = name_image.get_rect()
                screen.blit(start_bg_image, (0, 0))
                screen.blit(name_image, (width_1 // 2 - name_image_rect.width // 2, 100))
                screen.blit(loading_image[index], loading_rect)
                pygame.time.delay(300)
                index += 1
            elif index == 1:
                loading_rect.left, loading_rect.top = width_1 // 2 - 80, 300
                name_image_rect = name_image.get_rect()
                screen.blit(start_bg_image, (0, 0))
                screen.blit(name_image, (width_1 // 2 - name_image_rect.width // 2, 100))
                screen.blit(loading_image[index], loading_rect)
                pygame.time.delay(300)
                index += 1
            elif index == 2:
                loading_rect.left, loading_rect.top = width_1 // 2 - 80, 300
                name_image_rect = name_image.get_rect()
                screen.blit(start_bg_image, (0, 0))
                screen.blit(name_image, (width_1 // 2 - name_image_rect.width // 2, 100))
                screen.blit(loading_image[index], loading_rect)
                pygame.time.delay(300)
                index += 1
            elif index == 3:
                loading_rect.left, loading_rect.top = width_1 // 2 - 80, 300
                name_image_rect = name_image.get_rect()
                screen.blit(start_bg_image, (0, 0))
                screen.blit(name_image, (width_1 // 2 - name_image_rect.width // 2, 100))
                screen.blit(loading_image[index], loading_rect)
                pygame.time.delay(300)
                return None

        # 刷新屏幕
        delay -= 1
        pygame.display.update()
        pygame.display.flip()
        clock.tick(fps)


# 作者详情页的绘制
def dispaly_author():
    author_tx_rect = author_tx.get_rect()
    author_bf.set_alpha(150)
    author_tx_rect.left, author_tx_rect.top = width_2 // 2 - author_tx_rect.width // 2, 60
    pygame.display.set_caption("作者详情")
    if volume_cond:
        qzn_sound.play(1, fade_ms=1 * 1000)
        if not pygame.mixer.get_busy():
            wmzb_sound.play(1, fade_ms = 1 * 1000)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                qzn_sound.stop()
                wmzb_sound.stop()
                return None
        if pygame.display.get_active():
            screen.blit(author_bf, (0, 0))
            screen.blit(author_tx, author_tx_rect)
        # 刷新屏幕
        pygame.display.update()


def setting(volume, volume_2):
    # 生成音量框对象
    volume_rect = volume_image.get_rect()
    volume_rect_2 = volume_image.get_rect()
    volume_rect.centerx, volume_rect.centery = width_2 // 2 + 20, 280
    volume_rect_2.centerx, volume_rect_2.centery = width_2 // 2 + 20, volume_rect.height + 350

    # 生成音量杆对象
    volume_pole_rect = volume_pole.get_rect()
    volume_pole_rect2 = volume_pole.get_rect()
    volume_pole_rect.left, volume_pole_rect.top = volume_rect.left + volume * volume_rect.width, \
                                                    volume_rect.top - 5
    volume_pole_rect2.left, volume_pole_rect2.top = volume_rect_2.left + volume_2 * volume_rect.width, \
                                                        volume_rect_2.top - 5
    volume_fone = font_3.render("游戏音效  ", True, (0, 0, 0))
    volume_fone_rect = volume_fone.get_rect()
    volume_fone_rect.left, volume_fone_rect.bottom = volume_rect.left - volume_fone_rect.width, \
                                                        volume_rect.bottom + 10
    volume_fone2 = font_3.render("背景音乐  ", True, (0, 0, 0))
    volume_fone_rect2 = volume_fone2.get_rect()
    volume_fone_rect2.left, volume_fone_rect2.bottom = volume_rect_2.left - volume_fone_rect2.width, \
                                                         volume_rect_2.bottom + 8
    while True:
        pygame.display.set_caption("设置")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                return None
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and volume_rect.collidepoint(event.pos):
                    if volume_rect.left <= event.pos[0] <= volume_rect.right - volume_pole_rect.width:
                        volume_pole_rect.left = event.pos[0]
                    volume = (volume_pole_rect.left - volume_rect.left) / 135
                    user_getover.set_volume(volume)
                    get_bomb_sound.set_volume(volume)
                    get_double_sound.set_volume(volume)
                    bullet_sound.set_volume(volume)
                    get_bullet_sound.set_volume(volume)
                    button_sound.set_volume(volume)
                    enemy0_down_sound.set_volume(volume)
                    enemy1_down_sound.set_volume(volume)
                    enemy2_down_sound.set_volume(volume)
                    enemy2_appear_sound.set_volume(volume)
                    use_bomb_sound.set_volume(volume)
                if event.button == 1 and volume_rect_2.collidepoint(event.pos):
                    if volume_rect_2.left <= event.pos[0] <= volume_rect_2.right - volume_pole_rect2.width:
                        volume_pole_rect2.left = event.pos[0]
                    volume_2 = (volume_pole_rect2.left - volume_rect_2.left) / 135
                    pygame.mixer.music.set_volume(volume_2)
        # 绘制屏幕
        screen.blit(bg_image, (0, 0))
        screen.blit(volume_fone, volume_fone_rect)
        screen.blit(volume_fone2, volume_fone_rect2)
        screen.blit(volume_image, volume_rect)
        screen.blit(volume_image, volume_rect_2)
        screen.blit(volume_pole, volume_pole_rect)
        screen.blit(volume_pole, volume_pole_rect2)

        # 刷新屏幕
        pygame.display.flip()
        clock.tick(fps)


def main():
    # # 基本变量
    RED = (255, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    BLACK = (0, 0, 0)
    score = 0
    level = 1
    switch_alpha = 255
    life_number = 3
    index = [0, 0, 0, 0, 0, 0, 0]  # 包含玩家，小型敌人，中型敌人，大型敌人，初级子弹的索引, 双倍子弹索引, 载入游戏图片索引
    global delay, last_bomb, enemy_numbers, bullet_supply_numbers, bomb_supply_numbers, \
                double_bullet_time, volume_cond, volume, volume_2

    # #开关变量
    # 制造飞机动态变化的开关
    switch_image = True
    # 变化透明度的开关
    switch_alpha_cond = True
    # 生成双倍子弹开关
    is_double_bullet = False
    # 游戏开始界面的开关
    START = True
    # 游戏运行开关
    Running = True
    # 游戏结束画面的开关
    END = True
    # 按钮变换的开关
    button_switch = False
    button_2_switch = False
    # 读取历史纪录的开关
    read_score = True
    # 音量开关
    volume_cond = True

    # # 生成定时器模块
    # 双倍子弹计时器
    DOUBLE_BULLET_TIME = USEREVENT
    pygame.time.set_timer(DOUBLE_BULLET_TIME, 0 * 1000)
    # 我方无敌状态计时器
    WD_TIME = USEREVENT + 1
    pygame.time.set_timer(WD_TIME, 0 * 1000)
    # 显示历史分数的定时器
    DISPLAY_SCORE_TIME = USEREVENT + 2
    pygame.time.set_timer(DISPLAY_SCORE_TIME, 5 * 1000)

    # # 生成按钮对象
    # 生成暂停按钮对象
    pause_cond = False
    pause_switch = False
    paused_rect = paused_nor_image.get_rect()
    paused_rect.left, paused_rect.top = width_2 // 2 - paused_rect.width // 2, heigth_2 - paused_rect.height - 8
    # 生成炸弹按钮对象
    bomb_image_rect = bomb_image.get_rect()
    bomb_image_rect.left, bomb_image_rect.top = paused_rect.right + 50, paused_rect.top - 5
    # 生成音量按键对象
    music_switch = False
    music_image_rect = music_play_image.get_rect()
    music_image_rect.left, music_image_rect.top = width_2 - music_image_rect.width - 10, 66
    # 生成作者按键对象
    author_image = author_nor_image
    authon_image_rect = author_image.get_rect()
    authon_image_rect.left, authon_image_rect.top = width_2 - authon_image_rect.width - 10, 66 + 20 + music_image_rect.height
    # 生成设置按钮对象
    setting_image = setting_nor_image
    setting_rect = setting_image.get_rect()
    setting_rect.left, setting_rect.top = width_2 - setting_rect.width - 10, 66 + 40 + authon_image_rect.height + music_image_rect.height
    # 生成停止界面选项
    button_rect = button_not_image.get_rect()
    button_2_rect = button_not_image.get_rect()
    button_3_rect = button_not_image.get_rect()
    resume_font_rect = resume_font_image.get_rect()
    restart_font_rect = restart_font_image.get_rect()
    quit_font_rect = quit_font_image.get_rect()
    # # 生成对象模块组
    # 生成飞机对象模块
    player_plane = myplane.MyPlane(screen_2_size, screen)  # 玩家个人飞机
    # 生成敌方飞机的模块
    enemies = pygame.sprite.Group()  # 敌人总数组
    small_enemies = pygame.sprite.Group()
    add_small_enemies(small_enemies, enemies, int(enemy_numbers[0]))
    mid_enemies = pygame.sprite.Group()
    add_mid_enemies(mid_enemies, enemies, int(enemy_numbers[1]))
    big_enemies = pygame.sprite.Group()
    add_big_enemies(big_enemies, enemies, int(enemy_numbers[2]))
    # 生成初级子弹模块
    bullet_1 = []
    bullet_1_numbers = 5
    midtop = list(player_plane.rect.midtop)
    midtop[0] -= 10
    midtop[1] -= 12
    for n in range(bullet_1_numbers):
        bullet_1.append(bullets.Bullet_1(midtop))
    # 生成双倍子弹模块
    bullet_2 = []
    bullet_2_numbers = 10
    double_time = double_bullet_time
    left_button_pos = player_plane.rect.centerx - 33, player_plane.rect.centery - 25
    right_button_pos = player_plane.rect.centerx + 33, player_plane.rect.centery - 25
    for n in range(bullet_2_numbers):
        bullet_2.append(bullets.Bullet_2(left_button_pos))
        bullet_2.append(bullets.Bullet_2(right_button_pos))
    bullet_list = []
    # 生成道具模块
    supplies = pygame.sprite.Group()
    bullet_supply = supply.BulletSupply(screen, screen_2_size)
    supplies.add(bullet_supply)
    bomb_supply = supply.BombSupply(screen, screen_2_size)
    supplies.add(bomb_supply)
    SUPPLY_TIME = USEREVENT
    pygame.time.set_timer(SUPPLY_TIME, 30 * 1000)

    # 游戏的初始画面
    while START:

        pygame.display.set_caption("飞机大战--MGod吾 v1.0")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    action_image.set_alpha(0)
                    display_loading(index[6], delay)
                    pygame.display.set_mode(screen_2_size)
                    start_music.stop()
                    START = False
        # 绘制屏幕
        if pygame.display.get_active():
            start_music.play()
            action_image.set_alpha(switch_alpha)
            name_image_rect = name_image.get_rect()
            action_image_rect = action_image.get_rect()
            screen.blit(start_bg_image, (0, 0))
            screen.blit(action_image, (width_1 // 2 - action_image_rect.width // 2, 400))
            screen.blit(name_image, (width_1 // 2 - name_image_rect.width // 2, 100))
            if not (delay % 5):
                if switch_alpha_cond:
                    if switch_alpha > 0:
                        switch_alpha -= 3
                    else:
                        switch_alpha_cond = not switch_alpha_cond
                else:
                    if 255 - switch_alpha > 0:
                        switch_alpha += 3
                    else:
                        switch_alpha_cond = not switch_alpha_cond
        else:
            start_music.stop()
        # 刷新屏幕
        pygame.display.update()
        pygame.display.flip()
        clock.tick(fps)

    # 游戏人口
    while Running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if volume_cond:
                        button_sound.play()
                    pause_cond = not pause_cond
                    if pause_cond:
                        pygame.time.set_timer(SUPPLY_TIME, 0)
                        pygame.mixer.music.pause()
                        pygame.mixer.pause()
                    else:
                        pygame.mixer.music.unpause()
                        pygame.mixer.unpause()
                        pygame.time.set_timer(SUPPLY_TIME, 30 * 1000)
                elif event.key == pygame.K_q:
                    if last_bomb:
                        last_bomb -= 1
                        if volume_cond:
                            use_bomb_sound.play()
                        for enemy in enemies:
                            if enemy.rect.bottom > 0:
                                enemy.hp = 0
                elif event.key == pygame.K_e:
                    if volume_cond:
                        button_sound.play()
                    volume_cond = not volume_cond
                elif event.key == pygame.K_r:
                    if volume_cond:
                        button_sound.play()
                    dispaly_author()
                elif event.key == pygame.K_t:
                    if volume_cond:
                        button_sound.play()
                    setting(volume, volume_2)
            elif event.type == DOUBLE_BULLET_TIME and is_double_bullet and not pause_cond:
                if double_time:
                    double_time -= 1
            elif event.type == WD_TIME:
                player_plane.wd = False
            elif event.type == SUPPLY_TIME:
                if choice([True, False]):
                    bullet_supply.active = True
                    bullet_supply.start_pos()
                else:
                    bomb_supply.active = True
                    bomb_supply.start_pos()
            elif event.type == pygame.MOUSEMOTION:
                if paused_rect.collidepoint(event.pos):
                    pause_switch = True
                else:
                    pause_switch = False
                if button_rect.collidepoint(event.pos):
                    button_switch = True
                else:
                    button_switch = False
                if button_2_rect.collidepoint(event.pos):
                    button_2_switch = True
                else:
                    button_2_switch = False
                if music_image_rect.collidepoint(event.pos):
                    music_switch = True
                else:
                    music_switch = False
                if authon_image_rect.collidepoint(event.pos):
                    author_image = author_pressed_image
                else:
                    author_image = author_nor_image
                if setting_rect.collidepoint(event.pos):
                    setting_image = setting_pressed_image
                else:
                    setting_image = setting_nor_image
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and paused_rect.collidepoint(event.pos):
                    if volume_cond:
                        button_sound.play()
                    pause_cond = not pause_cond
                elif event.button == 1 and button_rect.collidepoint(event.pos):
                    if volume_cond:
                        button_sound.play()
                    pause_cond = not pause_cond
                elif event.button == 1 and button_2_rect.collidepoint(event.pos):
                    if volume_cond:
                        button_sound.play()
                    pygame.quit()
                    exit()
                elif event.button == 1 and music_image_rect.collidepoint(event.pos):
                    volume_cond = not volume_cond
                elif event.button == 1 and bomb_image_rect.collidepoint(event.pos):
                    if last_bomb:
                        last_bomb -= 1
                        if volume_cond:
                            use_bomb_sound.play()
                        for enemy in enemies:
                            if enemy.rect.bottom > 0:
                                enemy.hp = 0
                elif event.button == 1 and authon_image_rect.collidepoint(event.pos):
                    if volume_cond:
                        button_sound.play()
                    dispaly_author()
                elif event.button == 1 and setting_rect.collidepoint(event.pos):
                    if volume_cond:
                        button_sound.play()
                    setting(volume, volume_2)
        # 检测键盘按键事件
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_UP] or key_pressed[pygame.K_w]:
            player_plane.moveUP()
        elif key_pressed[pygame.K_DOWN] or key_pressed[pygame.K_s]:
            player_plane.moveDOWN()
        elif key_pressed[pygame.K_LEFT] or key_pressed[pygame.K_a]:
            player_plane.moveLEFT()
        elif key_pressed[pygame.K_RIGHT] or key_pressed[pygame.K_d]:
            player_plane.moveRIGHT()

        midtop = list(player_plane.rect.midtop)
        midtop[0] -= 10
        midtop[1] -= 12
        # 用于调整尾气切换的模块
        delay -= 1
        if not delay:
            delay = 100
        if not (delay % 5):
            switch_image = not switch_image
        screen.blit(bg_image, (0, 0))
        # 检测暂停按钮与恢复按钮的状态
        if not pause_cond:
            pause_image_1 = paused_nor_image
            pause_image_2 = paused_pressed_image
        else:
            pause_image_1 = resume_nor_image
            pause_image_2 = resume_pressed_image
        if not pause_switch:
            screen.blit(pause_image_1, paused_rect)
        else:
            screen.blit(pause_image_2, paused_rect)
        # 检测音量按键的状态
        if volume_cond:
            music_image_1 = music_play_image
            music_image_2 = music_play_image2
        else:
            music_image_1 = music_stop_image
            music_image_2 = music_stop_image2
        # 绘制得分项
        score_font = font.render(f"Score: {str(score)}", True, BLACK)
        screen.blit(score_font, (10, 5))
        # 绘制炸弹道具数量统计
        screen.blit(bomb_image, bomb_image_rect)
        last_bomb_font = font.render(f" x{str(last_bomb)}", True, BLACK)
        screen.blit(last_bomb_font, (bomb_image_rect.right + 5, bomb_image_rect.top + 10))
        # 绘制音量, 作者详情，设置按键
        if not music_switch:
            screen.blit(music_image_1, music_image_rect)
        else:
            screen.blit(music_image_2, music_image_rect)
        screen.blit(author_image, authon_image_rect)
        screen.blit(setting_image, setting_rect)
        # 绘制玩家生命剩余
        if life_number:
            for n in range(1, life_number + 1):
                screen.blit(life_image, ((width_2 // 2) // (life_number + 1) * n - 28, heigth_2 - 50))
        if is_double_bullet and not pause_cond:
            # 绘制双倍子弹剩余时间
            if double_time > 3:
                double_time_font = font.render(f"{str(double_time)}", True, BLACK)
            else:
                double_time_font = font.render(f"{str(double_time)}", True, RED)
            d_time_rect = double_time_font.get_rect()
            pygame.draw.circle(screen, WHITE, (width_2 - 41 + d_time_rect.centerx, 8 + d_time_rect.centery), 25)
            screen.blit(double_time_font, (width_2 - 40, 10))
        if not double_time:
            is_double_bullet = False
            pygame.time.set_timer(DOUBLE_BULLET_TIME, 0)
        # 依据得分改变游戏难度
        if score > 150000:
            if level == 1:
                level += 1
                add_number = [5, 3, 2]  # 小：15，中：8，大：4
                add_small_enemies(small_enemies, enemies, add_number[0])
                add_mid_enemies(mid_enemies, enemies, add_number[1])
                add_big_enemies(big_enemies, enemies, add_number[2])
        elif score > 500000:
            if level == 2:
                level += 1
                add_number = [10, 8, 5]  # 小：25，中：16，大：9
                add_small_enemies(small_enemies, enemies, add_number[0])
                add_mid_enemies(mid_enemies, enemies, add_number[1])
                add_big_enemies(big_enemies, enemies, add_number[2])
        elif score > 10000000:
            if level == 3:
                level += 1
                add_number = [10, 8, 5]  # 小：35，中：24，大：14
                add_small_enemies(small_enemies, enemies, add_number[0])
                add_mid_enemies(mid_enemies, enemies, add_number[1])
                add_big_enemies(big_enemies, enemies, add_number[2])

        # 当窗口呈现时并且暂停按钮不被按下时所要执行的代码
        if pygame.display.get_active():
            if not pause_cond:
                if volume_cond:
                    pygame.mixer.music.unpause()
                else:
                    pygame.mixer.music.pause()
                pygame.mixer.music.unpause()
                pygame.display.set_caption("正在游戏")
                # 检测玩家飞机是否与敌方飞机相撞
                bump_numbers = pygame.sprite.spritecollide(player_plane, enemies, False, pygame.sprite.collide_mask)
                if bump_numbers and not player_plane.wd:
                    if life_number:
                        life_number -= 1
                        if volume_cond:
                            user_getover.play()
                        player_plane.start_pos()
                        pygame.time.set_timer(WD_TIME, 3 * 1000)
                    for e in bump_numbers:
                        if not e.hp:
                            e.hp = 0
                # 判断玩家飞机是否存活
                if life_number:
                    if switch_image:
                        screen.blit(player_plane.plane_1, player_plane.rect)
                    else:
                        screen.blit(player_plane.plane_2, player_plane.rect)
                else:
                    if not index[0]:
                        if volume_cond:
                            user_getover.play()
                    if not (delay % 5):
                        screen.blit(player_plane.getover_image_list[index[0]], player_plane.rect)
                        index[0] = (index[0] + 1) % 4
                        if not index[0]:
                            pygame.mixer.pause()
                            pygame.mixer.music.pause()
                            pygame.time.delay(1 * 1000)
                            break
                # 发射子弹模块
                if not is_double_bullet:
                    bullet_list = bullet_1
                    if not (delay % 10):
                        bullet_1[index[4]].start_pos(midtop)
                        index[4] = (index[4] + 1) % bullet_1_numbers
                    elif not (delay % 10) and life_number:
                        if volume_cond:
                            bullet_sound.play()
                else:
                    bullet_list = bullet_2
                    if not (delay % 8):
                        bullet_2[index[5]].start_pos(
                            (player_plane.rect.centerx - 33, player_plane.rect.centery - 25))
                        bullet_2[index[5] + 1].start_pos(
                            (player_plane.rect.centerx + 30, player_plane.rect.centery - 25))
                        index[5] = (index[5] + 2) % bullet_2_numbers
                    elif not (delay % 8) and life_number:
                        if volume_cond:
                            bullet_sound.play()
                # 检测子弹是否存活
                for bullet in bullet_list:
                    if bullet.active:
                        screen.blit(bullet.bullet_image, bullet.rect)
                        bullet.move()
                        enemies_hit = pygame.sprite.spritecollide(bullet, enemies, False,
                                                                  pygame.sprite.collide_mask)
                        if enemies_hit:
                            bullet.active = False
                            for enemy in enemies_hit:
                                enemy.hit = True
                                if enemy.hp != 0:
                                    enemy.hp -= 1
                # 检测道具是否被获得
                get_supply = pygame.sprite.spritecollide(player_plane, supplies, False, pygame.sprite.collide_mask)
                if get_supply:
                    for s in get_supply:
                        if s == bomb_supply:
                            if volume_cond:
                                get_bomb_sound.play()
                            if last_bomb < 3:
                                last_bomb += 1
                        elif s == bullet_supply:
                            if volume_cond:
                                get_bomb_sound.play()
                            double_time = double_bullet_time
                            is_double_bullet = True
                            pygame.time.set_timer(DOUBLE_BULLET_TIME, 1 * 1000)
                        s.active = False
                        s.start_pos()
                # 生成道具模块
                if bullet_supply.active:
                    bullet_supply.appear()
                    bullet_supply.move()
                if bomb_supply.active:
                    bomb_supply.appear()
                    bomb_supply.move()
                # 生成敌方战舰
                for enemy in small_enemies:
                    if enemy.hp:
                        enemy.appear()
                        enemy.move()
                    elif not (delay % 3):
                        score += 500
                        if index[1] == 0:
                            if volume_cond:
                                enemy0_down_sound.play()
                        screen.blit(enemy.getover_image_list[index[1]], enemy.rect)
                        index[1] = (index[1] + 1) % 4
                        if index[1] == 0:
                            enemy.start_pos()
                for enemy in mid_enemies:
                    if enemy.hp:
                        if enemy.hit:
                            enemy.hit = False
                            enemy.get_hit()
                        else:
                            enemy.appear()
                        enemy.move()
                    elif not (delay % 3):
                        score += 2000
                        if index[2] == 0:
                            if volume_cond:
                                enemy1_down_sound.play()
                        screen.blit(enemy.getover_image_list[index[2]], enemy.rect)
                        index[2] = (index[2] + 1) % 4
                        if index[2] == 0:
                            enemy.start_pos()
                    # 绘制血条
                    pygame.draw.line(screen, WHITE, (enemy.rect.left, enemy.rect.bottom + 5),
                                     (enemy.rect.right, enemy.rect.bottom + 5), 2)
                    percent_hp = enemy.hp / 5
                    if percent_hp > 0.2:
                        hp_color = GREEN
                    else:
                        hp_color = RED
                    pygame.draw.line(screen, hp_color, (enemy.rect.left, enemy.rect.bottom + 5),
                                     (enemy.rect.left + enemy.rect.width * percent_hp, enemy.rect.bottom + 5), 2)
                for enemy in big_enemies:
                    if enemy.hp:
                        if enemy.rect.bottom == -40:
                            enemy2_appear_sound.play(-1)
                        if enemy.hit:
                            enemy.hit = False
                            enemy.get_hit()
                        elif switch_image:
                            enemy.switchimage1()
                        else:
                            enemy.switchimage2()
                        enemy.move()
                    elif not (delay % 3):
                        score += 50000
                        enemy2_appear_sound.stop()
                        if index[3] == 0:
                            if volume_cond:
                                enemy2_down_sound.play()
                        screen.blit(enemy.getover_image_list[index[3]], enemy.rect)
                        index[3] = (index[3] + 1) % 6
                        if index[3] == 0:
                            enemy.start_pos()
                    # 绘制血条
                    pygame.draw.line(screen, WHITE, (enemy.rect.left, enemy.rect.bottom + 5),
                                     (enemy.rect.right, enemy.rect.bottom + 5), 2)
                    percent_hp = enemy.hp / 15
                    if percent_hp > 0.2:
                        hp_color = GREEN
                    else:
                        hp_color = RED
                    pygame.draw.line(screen, hp_color, (enemy.rect.left, enemy.rect.bottom + 5),
                                     (enemy.rect.left + enemy.rect.width * percent_hp, enemy.rect.bottom + 5), 2)
            else:
                if not button_switch:
                    button_image_1 = button_not_image
                else:
                    button_image_1 = button_pressed_image
                if not button_2_switch:
                    button_image_2 = button_not_image
                else:
                    button_image_2 = button_pressed_image
                button_rect.left, button_rect.top = width_2 // 2 - button_rect.width // 2, 180
                button_2_rect.left, button_2_rect.top = width_2 // 2 - button_rect.width // 2, 180 + button_2_rect.height + 50
                resume_font_rect.center = button_rect.center
                quit_font_rect.center = button_2_rect.center
                screen.blit(button_image_1, button_rect)
                screen.blit(button_image_2, button_2_rect)
                screen.blit(resume_font_image, resume_font_rect)
                screen.blit(quit_font_image, quit_font_rect)
                pygame.display.set_caption("暂停游戏")
        else:
            pause_cond = True
            pygame.mixer.music.pause()
            pygame.mixer.pause()
        # 刷新屏幕
        pygame.display.update()
        pygame.display.flip()
        clock.tick(fps)

    # 玩家死亡的画面
    while END:
        if read_score:
            history_score = config["score"].getint("history_score")
            read_score = False
        # pygame.display.set_caption("游戏结束")
        is_most = set_history_score(score, history_score)
        screen.blit(get_over_image, (0, -80))
        history_score_font = font_2.render(str(history_score), True, BLACK)
        history_score_rect = history_score_font.get_rect()
        screen.blit(history_score_font, (width_2 // 2 - history_score_rect.width // 2, 200))
        if is_most:
            now_score_font = font_2.render(str(score), True, GREEN)
        else:
            now_score_font = font_2.render(str(score), True, RED)
        now_score_rect = now_score_font.get_rect()
        screen.blit(now_score_font, (width_2 // 2 - now_score_rect.width // 2, 520))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                pygame.display.set_mode(screen_1_size)
                read_score = True
                main()
                break
        # 刷新屏幕
        pygame.display.update()
        pygame.display.flip()
        clock.tick(fps)


if __name__ == '__main__':
    main()