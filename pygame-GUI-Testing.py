import pygame, random
pygame.init()
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT, K_ESCAPE, KEYDOWN, QUIT,)
# https://realpython.com/pygame-a-primer/

screen = pygame.display.set_mode([500, 500])
running = True
while running == True:

    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == pygame.K_a:
                pygame.draw.circle(screen, (100, 20, 190), (350, 350), 75)
        if event.type == pygame.MOUSEBUTTONDOWN:
#            circle_click = True if 
            pass

        if event.type == pygame.QUIT:
            running = False
        pygame.display.update()



pygame.quit()
