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



        self.tile1 = Tile("4", "1", "4", "1")
        self.tile2 = Tile("4", "1", "4", "2")
        self.tile3 = Tile("4", "1", "3", "1")
        self.tile4 = Tile("4", "1", "3", "2")
        self.tile5 = Tile("4", "2", "4", "1")
        self.tile6 = Tile("4", "2", "4", "4")
        self.tile7 = Tile("4", "2", "3", "1")
        self.tile8 = Tile("4", "2", "3", "2")
        self.tile9 = Tile("3", "1", "4", "1")
        self.tile10 = Tile("3", "1", "4", "2")
        self.tile11 = Tile("3", "1", "3", "1")
        self.tile12 = Tile("3", "1", "3", "2")
        self.tile13 = Tile("3", "2", "4", "1")
        self.tile14 = Tile("3", "2", "4", "2")
        self.tile15 = Tile("3", "2", "3", "1")
        self.tile16 = Tile("3", "2", "3", "2")

        self.tiles = [self.tile1, self.tile2, self.tile3, self.tile4, self.tile5, self.tile6, self.tile7,
                       self.tile8,self.tile9, self.tile10, self.tile11, self.tile12, self.tile13, self.tile14, self.tile15,
                       self.tile16]

    def fill(self, r, c):
        n = self.get_neighbors(r, c)
        color_tile = Tile()
        if n[0] is not None and self.grid[n[0][0]][n[0][1]] is not None:
            color_tile.t_c = self.grid[n[0][0]][n[0][1]].b_c

        if n[1] is not None and self.grid[n[1][0]][n[1][1]] is not None:
            color_tile.r_c = self.grid[n[1][0]][n[1][1]].l_c

        if n[2] is not None and self.grid[n[2][0]][n[2][1]] is not None:
            color_tile.b_c = self.grid[n[2][0]][n[2][1]].t_c

        if n[3] is not None and self.grid[n[3][0]][n[3][1]] is not None:
            color_tile.l_c = self.grid[n[3][0]][n[3][1]].r_c


        shuffled = self.tiles
        random.shuffle(shuffled)
        for tile in shuffled:
            if color_tile.matches(tile):
                self.grid[r][c] = tile
                return

    def create(self):
        for r in range(self.num_rows):
            for c in range(self.num_cols):
                self.fill(r, c)

    def in_bounds(self, r, c):
        return 0 <= r < self.num_rows and 0 <= c < self.num_cols

    def get_neighbors(self, r, c):
        neighbors = []
        neighbor_locs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        for neighbor_loc in neighbor_locs:
            if self.in_bounds(r + neighbor_loc[0], c + neighbor_loc[1]):
                neighbors.append([r + neighbor_loc[0], c + neighbor_loc[1]])
            else:
                neighbors.append(None)
        return neighbors

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        out = ""
        for i in range(self.num_rows):
            out += str(self.grid[i]) + "\n"
        return out
