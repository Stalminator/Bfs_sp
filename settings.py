import pygame, bfs

clock = pygame.time.Clock()

rect_size = 10
rect_number = 40
edge = rect_size * rect_number

win = pygame.display.set_mode((edge, edge))

game = True

black_rects = []
s_path = []
paths = []

start = (0, 1)
end = (0, 1)

graph = bfs.create_graph()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
TMP = (120,120,120)


def rect_pos(x_y):
    return (rect_size * (x_y[0] // rect_size), rect_size * (x_y[1] // rect_size))

def node_at_xy(x_y):
    return graph[2][x_y[1] // 10][x_y[0] // 10]
