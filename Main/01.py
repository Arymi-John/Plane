# coding: utf-8
# 作者:爱编程的章老师
# 创建:2021/1/28 8:48 下午
# 邮箱:slxxf000@163.com
# 微信:slxxfl
# 微信公众号:A卫隆少儿编程
# 格言:给自己的生活增加一份向上的力，每都进步一点点


import pygame
from sys import exit

WIDTH = 800
HEIGHT = 800
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("遮罩")
clock = pygame.time.Clock()

# 红色圆
red_circle = pygame.Surface((200, 200), pygame.SRCALPHA)
image01 = pygame.image.load('../IMages/plane.png')
image01 = pygame.transform.scale(image01, (76, 76))
image01 = pygame.transform.rotate(image01, angle=120)
red_circle.blit(image01, (0, 0))
# 红色圆的位置矩形
red_circle_rect = pygame.Rect(600, 0, 200, 200)  # 初位置位于屏幕左上角
m1 = pygame.mask.from_surface(red_circle)  # 生成红球的遮罩

# 蓝色圆
blue_circle = pygame.Surface((200, 200), pygame.SRCALPHA)
image02 = pygame.image.load('../IMages/yz.png')
# image02 = pygame.transform.scale(image02, (208, 236))
blue_circle.blit(image02, (0, 0))
# 蓝色圆的位置
blue_circle_rect = pygame.Rect(0, 600, 200, 200)  # 初位置位于屏幕右下角
m2 = pygame.mask.from_surface(blue_circle)  # 生成蓝球的遮罩

screen.blit(red_circle, red_circle_rect)
screen.blit(blue_circle, blue_circle_rect)
pygame.display.update()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    offset = blue_circle_rect.x - red_circle_rect.x, blue_circle_rect.y - red_circle_rect.y
    print(offset)
    p = m1.overlap(m2, offset)
    if not p:
        red_circle_rect.move_ip(-1, 1)
        blue_circle_rect.move_ip(1, -1)
        screen.fill("black")
        screen.blit(red_circle, red_circle_rect)
        screen.blit(blue_circle, blue_circle_rect)
        pygame.display.update()
    # 设置帧率
    clock.tick(60)
