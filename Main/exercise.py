import random
import math
import pygame
import sys
import time


class plane(object):
    def __init__(self):
        self.satue = 0
        self.plane_x = 262
        self.plane_y = 724
        self.old_x = self.plane_x
        self.dead = False
        self.plane_mask = pygame.Surface((76, 76), pygame.SRCALPHA)
        self.plane_rect = pygame.Rect(262, 724, 76, 76)
    def load(self):
        self.image = [pygame.image.load('../IMages/plane.png'),
                      pygame.image.load('../IMages/plane-1.png'),
                      pygame.image.load('../IMages/plane-2.png'),
                      pygame.image.load('../IMages/bang.png')]



    def update(self):
        self.plane_mask.fill('black')
        self.plane = pygame.transform.scale(self.image[self.satue], (76, 76))
        self.plane_mask.blit(self.plane, (0, 0))
        self.plane_ml = pygame.mask.from_surface(self.plane_mask)
        screen.blit(self.plane_mask, self.plane_rect)
        self.keylist = pygame.key.get_pressed()
        if self.keylist[pygame.K_a] and self.plane_x >= 0:
            self.plane_rect.move_ip(-5, 0)
            self.plane_x -= 5

        if self.keylist[pygame.K_d] and self.plane_x <= 524:
            self.plane_rect.move_ip(5, 0)
            self.plane_x += 5
        if self.keylist[pygame.K_w] and self.plane_y >= 0:
            self.plane_rect.move_ip(0, -5)
            self.plane_y -= 5

        if self.keylist[pygame.K_s] and self.plane_y <= 719:
            self.plane_rect.move_ip(0, 5)
            self.plane_y += 5

        if self.old_x > self.plane_x:
            self.satue = 2

        if self.old_x < self.plane_x:
            self.satue = 1

        if self.old_x == self.plane_x:
            self.satue = 0
        self.old_x = self.plane_x

        if not self.dead:
            if level.level == 0:
                bullet1.update()
            elif level.level == 1:
                bullet2.update()
            if boss.boss_flag:
                self.offset = boss.boss_rect.x - self.plane_rect.x, boss.boss_rect.y - self.plane_rect.y
                self.p = self.plane_ml.overlap(boss.boss_ml, self.offset)
                if self.p:
                    self.satue = 3
                    self.dead = True
                    screen.blit(self.plane_mask, self.plane_rect)
                if not self.p:
                    screen.blit(boss.boss_mask, boss.boss_rect)
                    boss.boss_rect.move_ip(0, 2)
                    boss.boss_y += 2

        if self.satue == 3:
            stop.update()


class bullet1(object):
    def __init__(self):
        self.image = pygame.image.load('../IMages/bullet.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (6, 12))
        self.bullet_x = []
        self.bullet_y = []
        self.bullet_mask = pygame.Surface((6, 12))
        self.delay = 100

    def update(self):
        if self.delay % 5 == 0:
            self.bullet_x.append(plane.plane_x + 38)
            self.bullet_y.append(plane.plane_y)
            self.sound = pygame.mixer.Sound('../Studio/platk.wav')
            pygame.mixer.Sound.play(self.sound)

        for i in range(len(self.bullet_y) - 1):
            self.bullet_mask.blit(self.image, (0, 0))
            screen.blit(self.bullet_mask, (self.bullet_x[i], self.bullet_y[i], 6, 12))


        for i in range(len(self.bullet_y) - 1):
            self.bullet_y[i] -= 10
        for i in range(len(self.bullet_y) - 1):
            self.offset = boss.boss_rect.x - self.bullet_x[i], boss.boss_y - self.bullet_y[i]
            self.bullet_ml= pygame.mask.from_surface(self.bullet_mask)
            self.p = self.bullet_ml.overlap(boss.boss_ml, self.offset)
            if self.p:
                boss.Hp -= 1
                del self.bullet_x[i]
                del self.bullet_y[i]
                break
            elif self.bullet_y[i] <= 10:
                del self.bullet_x[i]
                del self.bullet_y[i]
                break


        self.delay -= 1
        if not self.delay:
            self.delay = 100


class bullet2(object):
    def __init__(self):
        self.image = pygame.image.load('../IMages/bullet.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (6, 12))
        self.image2 = pygame.transform.rotate(self.image, angle=30)
        self.image3 = pygame.transform.rotate(self.image, angle=150)
        self.bullet_x = []
        self.bullet_y = []
        self.b = []
        self.delay = 100

    def update(self):
        if self.delay % 5 == 0:
            self.bullet_x.append(plane.plane_x + 38)
            self.bullet_y.append(plane.plane_y)
            self.b.append((2 + math.sqrt(3)) * plane.plane_x - plane.plane_y)
            self.sound = pygame.mixer.Sound('../Studio/platk.wav')
            pygame.mixer.Sound.play(self.sound)


        for i in range(len(self.bullet_y) - 1):
            screen.blit(self.image, (self.bullet_x[i], self.bullet_y[i]))
            screen.blit(self.image2, (bullet2.move(self.bullet_y[i], self.b[i]), self.bullet_y[i]))
            screen.blit(self.image3, (self.bullet_x[i] - (bullet2.move(self.bullet_y[i], self.b[i])) + self.bullet_x[i], self.bullet_y[i]))

        for i in range(len(self.bullet_y) - 1):
            self.bullet_y[i] -= 10
        for i in range(len(self.bullet_y) - 1):
            if self.bullet_y[i] > boss.boss_y:
                if self.bullet_y[i] < boss.boss_y + 128 and self.bullet_x[i] > boss.boss_x and self.bullet_x[
                    i] < boss.boss_x + 180 and boss.boss_flag:
                    boss.Hp -= 1
                    del self.bullet_x[i]
                    del self.bullet_y[i]
                    del self.b[i]
                    break
            elif self.bullet_y[i] <= 10:
                del self.bullet_x[i]
                del self.bullet_y[i]
                del self.b[i]
                break

        self.delay -= 1
        if not self.delay:
            self.delay = 100

    def move(self, y, b):
        self.y = y
        self.x = (self.y + b) / (2 + math.sqrt(3))
        return self.x


class Boss1(object):
    def __init__(self):
        self.boss_y = -100
        self.Hp = 20
        self.boss_flag = False
        self.boss_x = random.randint(0, 400)
        self.boss_image = pygame.image.load('../IMages/yz.png').convert_alpha()
        self.boss_image = pygame.transform.scale(self.boss_image, (200, 200))
        self.boss_mask = pygame.Surface((208, 236), pygame.SRCALPHA)
        self.boss_mask.blit(self.boss_image, (0, 0))
        self.boss_ml = pygame.mask.from_surface(self.boss_mask)
        self.boss_rect = pygame.Rect(self.boss_x, self.boss_y, 208, 236)

    def update(self):
        if self.Hp > 0:
            self.boss_flag = True
        elif self.boss_flag:
            self.boss_flag = False
            score.num += 1
        if self.boss_y >= 1000 or not self.boss_flag:
            self.boss_x = random.randint(0, 400)
            self.boss_y = -100
            self.Hp = 20
            self.boss_rect = pygame.Rect(self.boss_x, self.boss_y, 208, 236)


class Score(object):
    def __init__(self):
        self.num = 0
        self.font = pygame.font.SysFont(None, 60)

    def update(self):
        self.test = self.font.render(str(self.num), True, ('red'), None)
        screen.blit(self.test, (10, 10))


class Stop(object):
    def __init__(self):
        self.x = 50
        self.y = 0
        self.clock = clock = pygame.time.Clock()
    def update(self):
        self.flag = False
        while True:
            self.image = pygame.image.load('../IMages/gameover.png')
            self.image = pygame.transform.scale(self.image, (500, 100))
            bmg = pygame.image.load('../IMages/??????.png')
            screen.blit(bmg, (0, 0))
            screen.blit(self.image, (self.x, self.y))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.flag = True

            self.ticks = pygame.time.get_ticks()
            if self.ticks % 1 == 0:
                self.y += 0.5
            pygame.display.flip()
            self.clock.tick(60)
            if self.flag:
                break


class level(object):
    def __init__(self):
        self.level = 0
        self.level1 = pygame.image.load('../IMages/up.png')
        self.level1 = pygame.transform.scale(self.level1, (50, 50))
        self.x = 50
        self.y = -50
        self.flag = False

    def update(self):
        if  not self.flag:
            screen.blit(self.level1, (self.x, self.y))

        if (plane.plane_x + 76 >= self.x) and (plane.plane_x < self.x + 50) and (
            plane.plane_y - self.y) <= 25 and (plane.plane_y - self.y) >= 0:
            self.flag = True
            self.level = 1
            self.x = random.randint(0, 750)
            self.y = -50

        else:
            self.y += 3


if __name__ == '__main__':
    pygame.init()
    pygame.display.init()
    pygame.mixer.music.load('../Studio/bgm.mp3')
    pygame.mixer.music.play(-1)
    screen = pygame.display.set_mode(size=(600, 800))
    plane = plane()
    bullet1 = bullet1()
    bullet2 =bullet2()
    score = Score()
    boss = Boss1()
    stop = Stop()
    level = level()
    plane.load()
    clock = pygame.time.Clock()


    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        bmg = pygame.image.load('../IMages/??????.png')
        screen.blit(bmg, (0, 0))

        plane.update()
        score.update()
        boss.update()
        level.update()
        pygame.display.flip()
        clock.tick(60)