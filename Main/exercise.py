import pygame
import sys

pygame.init()
pygame.display.init()
screen = pygame.display.set_mode(size=(600, 800))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.flip()