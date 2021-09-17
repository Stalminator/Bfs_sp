import pygame

def draw_rect(win,COLOR,rect_size,rects_list):
    for i in rects_list:
        pygame.draw.rect(win, COLOR, (i[0] + 1, i[1] + 1, rect_size - 1, rect_size - 1))

def draw_lines(win, COLOR, edge, rect_size):
    for i in range(0, edge, rect_size):
        pygame.draw.line(win, COLOR, (0, i), (edge, i))
        pygame.draw.line(win, COLOR, (i, 0), (i, edge))

def mouse_buttons(mouse_pos,rect_pos,black_rects):
    if pygame.mouse.get_pressed()[0]:
        if rect_pos(mouse_pos) not in black_rects:
            black_rects.append(rect_pos(mouse_pos))
    if pygame.mouse.get_pressed()[2]:
        if rect_pos(mouse_pos) in black_rects:
            black_rects.remove(rect_pos(mouse_pos))

def draw_start_end(start,end,RED,BLUE,rect_size,win):
    if start != (0, 0):
        pygame.draw.rect(win, RED, (start[0] + 1, start[1] + 1, rect_size - 1, rect_size - 1))
    if end != (0, 0):
        pygame.draw.rect(win, BLUE, (end[0] + 1, end[1] + 1, rect_size - 1, rect_size - 1))