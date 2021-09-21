import pygame
import pygame_functions as pf, bfs

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

black_rects = []
s_path = []

start = (0, 1)
end = (0, 1)

graph, nodes_pos, nodes = bfs.create_graph(rect_number)

# calculating right x and y for single rect draw
def rect_pos(x_y):
    return (rect_size * (x_y[0] // rect_size), rect_size * (x_y[1] // rect_size))

while game:
    win.fill(WHITE)
    clock.tick(60)
    mouse_pos = pygame.mouse.get_pos()
    pf.mouse_buttons(mouse_pos, rect_pos, black_rects)
    if pygame.mouse.get_pressed()[2]:
        graph, nodes_pos, nodes = bfs.create_graph(rect_number)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0:
                s_path.clear()
                path = bfs.bfs_path(graph, nodes[start[1] // 10][start[0] // 10], nodes[end[1] // 10][end[0] // 10])
                if path:
                    for i in path:
                        s_path.append((nodes_pos[i][1] * 10, nodes_pos[i][0] * 10))
                    s_path = s_path[1:-1]
                else:
                    print('No path')
            if event.key == pygame.K_w:
                s_path.clear()
            if event.key == pygame.K_1:
                start = rect_pos(mouse_pos)
            if event.key == pygame.K_2:
                end = rect_pos(mouse_pos)
            if event.key == pygame.K_s:
                s_path.clear()

    pf.draw_lines(win, BLACK, edge, rect_size)
    pf.draw_rect(win, GREEN, rect_size, s_path)
    pf.draw_rect(win, BLACK, rect_size, black_rects)
    pf.draw_start_end(start, end, RED, BLUE, rect_size, win)

    bfs.graph_update(black_rects, graph, nodes)

    pygame.display.update()