import turtle
import math
from tile import *

cell_size = 100


def draw_pattern(grid):
    num_rows = len(grid)
    num_cols = len(grid[0])

    screen_width = cell_size * num_cols
    screen_height = cell_size * num_rows

    screen = turtle.getscreen()
    screen.setup(screen_width, screen_height)

    dave = turtle.Turtle()
    dave.speed(0)
    dave.penup()
    dave.goto(-screen_width / 2, screen_height / 2)

    print("Turtle pos: {}".format(dave.pos()))

    for r in range(num_rows):
        for c in range(num_cols):
            if grid[r][c]:

                draw_tile(dave, grid[r][c])
            else:
                draw_tile(dave, Tile())
        dave.penup()
        dave.backward(screen_width)
        dave.right(90)
        dave.forward(cell_size)
        dave.left(90)
    input()


def draw_tile(dave, tile):
    dave.setheading(0)
    draw_triangle(dave, tile.t_c)
    dave.forward(cell_size)
    dave.right(90)

    draw_triangle(dave, tile.r_c)
    dave.forward(cell_size)
    dave.right(90)

    draw_triangle(dave, tile.b_c)
    dave.forward(cell_size)
    dave.right(90)

    draw_triangle(dave, tile.l_c)
    dave.forward(cell_size)
    dave.right(90)
    dave.forward(cell_size)


def draw_triangle(dave, color):
    dist1 = cell_size
    dist2 = cell_size * math.sqrt(2) / 2

    dave.pendown()
    if color == None:
        dave.fillcolor("white")
    else:
        dave.fillcolor(color)
    dave.begin_fill()
    dave.forward(dist1)
    dave.right(135)
    dave.forward(dist2)
    dave.right(90)
    dave.forward(dist2)
    dave.right(135)
    dave.end_fill()
    dave.penup()
