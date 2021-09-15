import time

import pygame, random

pygame.init()
clock = pygame.time.Clock()

edge = 401
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
rect_size = 10

win = pygame.display.set_mode((edge, edge))

game = True

l = []

start, end = (0, 0), (0, 0)

while game:
    win.fill(WHITE)
    clock.tick(120)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())
            l.append(pygame.mouse.get_pos())

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0:
                print(pygame.mouse.get_pos())
            if event.key == pygame.K_1:
                start = pygame.mouse.get_pos()
            if event.key == pygame.K_2:
                end = pygame.mouse.get_pos()
            if event.key == pygame.K_s:
                print(start, end)
    for i in range(0, edge, rect_size):
        pygame.draw.line(win, BLACK, (0, i), (edge, i))
        pygame.draw.line(win, BLACK, (i, 0), (i, edge))
    if pygame.mouse.get_pressed():
        l.append(pygame.mouse.get_pos())
    # time.sleep(0.4)

    # pygame.draw.rect(win,WHITE,(random.randrange(1,edge,10),random.randrange(1,edge,10),9,9))
    for i in l:
        pygame.draw.rect(win, BLACK, (
                rect_size * (i[0] // rect_size) + 1, rect_size * (i[1] // rect_size) + 1, rect_size - 1, rect_size - 1))

    if start != (0,0):
        pygame.draw.rect(win, RED, (
                rect_size * (start[0] // rect_size) + 1, rect_size * (start[1] // rect_size) + 1, rect_size - 1, rect_size - 1))
    if end != (0,0):
        pygame.draw.rect(win, BLUE, (
                rect_size * (end[0] // rect_size) + 1, rect_size * (end[1] // rect_size) + 1, rect_size - 1, rect_size - 1))


    # pygame.draw.rect(win, WHITE, (10 * (pygame.mouse.get_pos()[0] // 10) + 1, 10 * (pygame.mouse.get_pos()[1] // 10) + 1, 9, 9))
    #l.append(pygame.mouse.get_pos())
    pygame.display.update()
