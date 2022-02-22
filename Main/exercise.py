import pygame
import sys

if __name__ == '__main__':
    pygame.init()
    pygame.display.init()
    screen = pygame.display.set_mode(size=(600, 800))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        bmg = pygame.image.load('../IMages/背景.png')
        screen.blit(bmg, (0, 0))

        pygame.display.flip()