import pygame
import pygame_functions as pf, bfs, settings as s

pygame.init()
clock = pygame.time.Clock()

while s.game:
    s.win.fill(s.WHITE)
    clock.tick(60)
    mouse_pos = pygame.mouse.get_pos()
    pf.mouse_buttons(mouse_pos)
    if pygame.mouse.get_pressed()[2]:
        s.graph = bfs.create_graph()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            s.game = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0:
                s.s_path.clear()
                path = bfs.bfs_path()
                if path:
                    for i in path:
                        s.s_path.append((s.graph[1][i][1] * 10, s.graph[1][i][0] * 10))
                    s.s_path = s.s_path[1:-1]
                else:
                    print('No path')
            if event.key == pygame.K_w:
                s.s_path.clear()
            if event.key == pygame.K_1:
                s.start = s.rect_pos(mouse_pos)
            if event.key == pygame.K_2:
                s.end = s.rect_pos(mouse_pos)
            if event.key == pygame.K_s:
                s.s_path.clear()

    pf.draw_lines()
    pf.draw_rect(s.GREEN, s.s_path)
    pf.draw_rect(s.BLACK, s.black_rects)
    pf.draw_start_end()

    bfs.graph_update()

    pygame.display.update()
