import pygame
import sys
import time


class plane(object):
    def __init__(self):
        self.satue = 0
        self.plane_x = 262
        self.plane_y = 724
        self.old_x = self.plane_x

    def load(self):
        self.image = [pygame.image.load('../IMages/plane.png'),
                      pygame.image.load('../IMages/plane-1.png'),
                      pygame.image.load('../IMages/plane-2.png')]

    def update(self):
        self.plane = self.image[self.satue].convert_alpha()
        self.plane = pygame.transform.scale(self.plane, (76, 76))
        screen.blit(self.plane, (self.plane_x, self.plane_y))
        self.keylist = pygame.key.get_pressed()
        if self.keylist[pygame.K_a] and self.plane_x >= 0:
            self.plane_x -= 5

        if self.keylist[pygame.K_d] and self.plane_x <= 524:
            self.plane_x += 5

        if self.keylist[pygame.K_w] and self.plane_y >= 0:
            self.plane_y -= 5

        if self.keylist[pygame.K_s] and self.plane_y <= 719:
            self.plane_y += 5

        if self.old_x > self.plane_x:
            self.satue = 2

        if self.old_x < self.plane_x:
            self.satue = 1

        if self.old_x == self.plane_x:
            self.satue = 0

        self.old_x = self.plane_x
        bullet1.update()

class bullet1(object):
    def __init__(self):
        self.image = pygame.image.load('../IMages/bullet.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (6, 12))
        self.bullet_x = []
        self.bullet_y = []
        self.delay = 100

    def update(self):
        if self.delay % 5 == 0:
            self.bullet_x.append(plane.plane_x + 38)
            self.bullet_y.append(plane.plane_y)
            self.sound = pygame.mixer.Sound('../Studio/platk.wav')
            pygame.mixer.Sound.play(self.sound)

        for i in range(len(self.bullet_y) - 1):
            screen.blit(self.image, (self.bullet_x[i], self.bullet_y[i]))

        for i in range(len(self.bullet_y) - 1):
            self.bullet_y[i] -= 10
        for i in range(len(self.bullet_y) - 1):
            if self.bullet_y[i] < boss.boss_y + 128 and self.bullet_x[i] > boss.boss_x and self.bullet_x[i] < boss.boss_x + 206 and boss.boss_flag:
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

class Boss1(object):
    def __init__(self):
        self.boss_x = 300
        self.boss_y = 0
        self.Hp = 10
        self.boss_flag = False

    def update(self):
        self.boss_image = pygame.image.load('../IMages/yz.png').convert_alpha()
        self.boss_image = pygame.transform.scale(self.boss_image, (208, 236))
        if score.score % 100 == 0 and self.Hp > 0:
            self.boss_flag = True

        else:
            self.boss_flag = False
        if self.boss_flag:
            screen.blit(self.boss_image, (self.boss_x, self.boss_y))
            self.boss_y += 2





class Score(object):
    def __init__(self):
        self.score = 0
        self.font = pygame.font.SysFont(None, 60)

    def update(self):
        self.test = self.font.render(str(self.score), True, ('red'), None)
        screen.blit(self.test, (10, 10))






if __name__ == '__main__':
    pygame.init()
    pygame.display.init()
    screen = pygame.display.set_mode(size=(600, 800))
    plane = plane()
    bullet1 = bullet1()
    score = Score()
    boss = Boss1()
    plane.load()
    clock = pygame.time.Clock()

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        bmg = pygame.image.load('../IMages/背景.png')
        screen.blit(bmg, (0, 0))
        plane.update()
        score.update()
        boss.update()
        pygame.display.flip()
        clock.tick(60)