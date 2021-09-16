import time

import pygame, pygame_functions as pf, bfs

pygame.init()
clock = pygame.time.Clock()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

rect_size = 10
rect_number = 40
edge = rect_size * rect_number

win = pygame.display.set_mode((edge, edge))

game = True

l = []
w = []

start = (0, 0)
end = (0, 0)


# calculatin rigth x and y for single rect draw
def rect_pos(x_y):
    return (rect_size * (x_y[0] // rect_size), rect_size * (x_y[1] // rect_size))


while game:
    win.fill(WHITE)
    clock.tick(60)
    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

        if pygame.mouse.get_pressed()[0]:
            if rect_pos(mouse_pos) not in l:
                l.append(rect_pos(mouse_pos))
        if pygame.mouse.get_pressed()[2]:
            if rect_pos(mouse_pos) in l:
                l.remove(rect_pos(mouse_pos))

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0:
                w.clear()
                path = bfs.bfs_path(bfs.a, bfs.c[start[1]//10][start[0]//10], bfs.c[end[1]//10][end[0]//10])

                for i in path:
                    w.append((bfs.b[i][1] * 10, bfs.b[i][0] * 10))
            if event.key == pygame.K_w:
                w.clear()
            if event.key == pygame.K_1:
                start = rect_pos(mouse_pos)
            if event.key == pygame.K_2:
                end = rect_pos(mouse_pos)
            if event.key == pygame.K_s:
                print(start, end)
            #if event.key == pygame.K_c:
                #bfs.bfs_path

    for i in range(0, edge, rect_size):
        pygame.draw.line(win, BLACK, (0, i), (edge, i))
        pygame.draw.line(win, BLACK, (i, 0), (i, edge))

    # time.sleep(0.4)

    for i in l:
        pf.draw_rect(win, BLACK, i, rect_size)

    if start != (0, 0):
        pf.draw_rect(win, RED, start, rect_size)
    if start != (0, 0):
        pf.draw_rect(win, BLUE, end, rect_size)

    for i in l:
        if bfs.c[i[1]//10][i[0]//10] in bfs.a:
            del bfs.a[bfs.c[i[1]//10][i[0]//10]]
        for j in bfs.a.values():
            if bfs.c[i[1]//10][i[0]//10] in j:
                j.remove(bfs.c[i[1]//10][i[0]//10])


    for i in w:
        pf.draw_rect(win, GREEN, (i[0],i[1]), rect_size)

    pygame.display.update()
