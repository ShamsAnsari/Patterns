import random
import colour
from tile import *


class Grid:
    def __init__(self, num_rows, num_cols):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.grid = []
        for i in range(num_rows):
            self.grid.append([None] * num_cols)

        self.tile1 = Tile("red", "red", "red", "green")
        self.tile2 = Tile("blue", "red", "blue", "green")
        self.tile3 = Tile("red", "green", "green", "green")
        self.tile4 = Tile("white", "blue", "red", "blue")
        self.tile5 = Tile("blue", "blue", "white", "blue")
        self.tile6 = Tile("white", "white", "red", "white")
        self.tile7 = Tile("red", "green", "blue", "white")
        self.tile8 = Tile("blue", "white", "blue", "red")
        self.tile9 = Tile("blue", "red", "white", "red")
        self.tile10 = Tile("green", "green", "blue", "red")
        self.tile11 = Tile("red", "white", "red", "green")

        self.tiles = [self.tile1, self.tile2, self.tile3, self.tile4, self.tile5, self.tile6, self.tile7,
                      self.tile8, self.tile9, self.tile10, self.tile11]

    def fill(self, r, c):
        neighbors = self.get_neighbors(r, c)
        color_tile = Tile()
        if neighbors[0] is not None:
            color_tile.t_c = neighbors[0].b_c
        if neighbors[1] is not None:
            color_tile.r_c = neighbors[1].l_c
        if neighbors[2] is not None:
            color_tile.b_c = neighbors[2].t_c
        if neighbors[3] is not None:
            color_tile.l_c = neighbors[3].r_c

        correct_tile = None
        for tile in self.tiles:
            if color_tile.matches(tile):
                correct_tile = tile
        if correct_tile is not None:
            self.grid[r][c] = correct_tile

    def create(self):
        for r in range(self.num_rows):
            for c in range(self.num_cols):
                self.fill(r, c)

    def in_bounds(self, r, c):
        return 0 <= r < self.num_rows and 0 <= c < self.num_cols

    def get_neighbors(self, r, c):
        neighbors = []
        neighbor_locs = [[-1, 0], [0, 1], [-1, 0], [0, -1]]
        for neighbor_loc in neighbor_locs:
            if self.in_bounds(r + neighbor_loc[0], c + neighbor_loc[1]):
                neighbors.append([r + neighbor_loc[0], c + neighbor_loc[1]])
            else:
                neighbors.append(None)
        return neighbors

    def print_grid(self):
        for i in range(self.num_rows):
            print(self.grid[i])
