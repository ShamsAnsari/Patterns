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

        # self.tile1 = Tile("green", "green", "blue", "red")
        # self.tile2 = Tile("green", "blue", "green", "red")
        # self.tile3 = Tile("green", "blue", "blue", "green")
        # self.tile4 = Tile("red", "red", "green", "green")
        # self.tile5 = Tile("red", "red", "blue","blue")
        # self.tile6 = Tile("red", "green", "green", "blue")
        # self.tile7 = Tile("yellow", "yellow", "red","yellow")
        # self.tile8 = Tile("blue", "yellow", "green", "yellow")
        # self.tile9 = Tile("green", "white", "red", "yellow")
        # self.tile10 = Tile("green", "white", "yellow", "yellow")
        # self.tile11 = Tile("yellow", "white", "red", "white")
        # self.tile12 = Tile("blue", "white", "green", "white")
        # self.tile13 = Tile("green", "yellow", "green", "white")
        #
        #
        # self.tiles = [self.tile1, self.tile2, self.tile3, self.tile4, self.tile5, self.tile6, self.tile7,
        #               self.tile8, self.tile9, self.tile10, self.tile11, self.tile12, self.tile13]

    def fill(self, r, c):
        n = self.get_neighbors(r, c)
        color_tile = Tile()
        print(n)
        if n[0] is not None and self.grid[n[0][0]][n[0][1]] is not None:
            color_tile.t_c = self.grid[n[0][0]][n[0][1]].b_c

        if n[1] is not None and self.grid[n[1][0]][n[1][1]] is not None:
            color_tile.r_c = self.grid[n[1][0]][n[1][1]].l_c

        if n[2] is not None and self.grid[n[2][0]][n[2][1]] is not None:
            color_tile.b_c = self.grid[n[2][0]][n[2][1]].t_c

        if n[3] is not None and self.grid[n[3][0]][n[3][1]] is not None:
            color_tile.l_c = self.grid[n[3][0]][n[3][1]].r_c


        for tile in self.tiles:
            if color_tile.matches(tile):
                self.grid[r][c] = tile
                return
        print("No match:{},{} {}".format(r,c ,color_tile))

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
