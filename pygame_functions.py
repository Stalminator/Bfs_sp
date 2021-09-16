import pygame

def draw_rect(win,COLOR,x_y,rect_size):
    pygame.draw.rect(win, COLOR, (
        x_y[0] + 1, x_y[1] + 1, rect_size - 1, rect_size - 1))