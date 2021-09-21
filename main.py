import pygame
import pygame_functions as pf, bfs, settings as s

pygame.init()

while s.game:
    s.win.fill(s.WHITE)
    s.clock.tick(120)
    mouse_pos = pygame.mouse.get_pos()
    pf.mouse_buttons(mouse_pos)

    pf.events(mouse_pos)

    pf.draw()

    bfs.graph_update()

    pygame.display.update()
