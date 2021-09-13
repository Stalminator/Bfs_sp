import time

import pygame, random

pygame.init()
clock = pygame.time.Clock()

edge = 401
BLACK = (0,0,0)
WHITE = (255,255,255)


win = pygame.display.set_mode((edge,edge))

game = True

l = []

while game:
    win.fill(BLACK)
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())
            l.append(pygame.mouse.get_pos())
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0:
                print(pygame.mouse.get_pos())
    for i in range(0,edge,10):
        pygame.draw.line(win,WHITE,(0,i),(edge,i))
        pygame.draw.line(win, WHITE, (i, 0), (i, edge))

    #time.sleep(0.4)

    #pygame.draw.rect(win,WHITE,(random.randrange(1,edge,10),random.randrange(1,edge,10),9,9))
    for i in l:
        pygame.draw.rect(win,WHITE,(10*(i[0]//10)+1,10*(i[1]//10)+1,9,9))
    #pygame.draw.rect(win, WHITE, (10 * (pygame.mouse.get_pos()[0] // 10) + 1, 10 * (pygame.mouse.get_pos()[1] // 10) + 1, 9, 9))
    l.append(pygame.mouse.get_pos())
    pygame.display.update()