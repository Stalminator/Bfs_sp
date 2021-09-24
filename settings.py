#file to store all variables and settings

import pygame, bfs

clock = pygame.time.Clock()

#single rectangle size
rect_size = 20

#number of rectangles
rect_number = 40

#size of main app windows
edge = rect_size * rect_number

#main pygame window
win = pygame.display.set_mode((edge, edge))

game = True

#list of black rectangle
black_rects = []

#shortest path list
s_path = []

#all paths during finding shirtest path
paths = []

#start of the shortest path
start = (0, 1)

#end of the shortest path
end = (0, 1)

#main graph
graph = bfs.create_graph()

#colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
GREY = (120,120,120)

#converting real cursor position over specific rectangle to position where rectangle will be draw
def rect_pos(x_y):
    return (rect_size * (x_y[0] // rect_size), rect_size * (x_y[1] // rect_size))

#obtaining which nodes is under the mouse cursor
def node_at_xy(x_y):
    return graph[2][x_y[1] // rect_size][x_y[0] // rect_size]
