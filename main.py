import random


class Tile:
    def __init__(self):
        self.__init__(None, None, None, None)

    def __init__(self, top_color, right_color, bottom_color, left_color):
        self.t_c = top_color
        self.r_c = right_color
        self.b_c = bottom_color
        self.l_c = left_color

    def matches(self, tile):
        if self.t_c is not None and tile.t_c is not None and self.t_c != tile.t_c:
            return False
        if self.r_c is not None and tile.r_c is not None and self.r_c != tile.r_c:
            return False
        if self.b_c is not None and tile.b_c is not None and self.b_c != tile.b_c:
            return False
        if self.l_c is not None and tile.l_c is not None and self.l_c != tile.l_c:
            return False
        return True

    def __repr__(self):
        return "t_c: {}, r_c: {}, b_c: {}, l_c: {}".format(self.t_c, self.r_c, self.b_c, self.l_c)

    def __str__(self):
        return self.__repr__()


class Grid:
    def __init__(self, num_rows, num_cols):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.grid = []
        for i in range(num_rows):
            self.grid.append([None] * num_cols)

        self.red = (255, 0, 0)
        self.green = (0, 255, 0)
        self.blue = (0, 0, 255)
        self.white = (0, 0, 0)

        self.tile1 = Tile(self.red, self.red, self.red, self.green)
        self.tile2 = Tile(self.blue, self.red, self.blue, self.green)
        self.tile3 = Tile(self.red, self.green, self.green, self.green)
        self.tile4 = Tile(self.white, self.blue, self.red, self.blue)
        self.tile5 = Tile(self.blue, self.blue, self.white, self.blue)
        self.tile6 = Tile(self.white, self.white, self.red, self.white)
        self.tile7 = Tile(self.red, self.green, self.blue, self.white)
        self.tile8 = Tile(self.blue, self.white, self.blue, self.red)
        self.tile9 = Tile(self.blue, self.red, self.white, self.red)
        self.tile10 = Tile(self.green, self.green, self.blue, self.red)
        self.tile11 = Tile(self.red, self.white, self.red, self.green)

        self.tiles = [self.tile1, self.tile2, self.tile3, self.tile4, self.tile5, self.tile6, self.tile7,
                      self.tile8, self.tile9, self.tile10, self.tile11]

    def create(self):
        self.grid[0][0] = self.tiles[random.randrange(0, 11)]

        for r in range(self.num_rows):
            for c in range(self.num_cols):
                if r == 0 and c == 0:
                    continue

                colors = []
                for i, neighbor in enumerate(self.get_neighbors(r, c)):

                    if neighbor is None or self.grid[neighbor[0]][neighbor[1]] is None:
                        colors.append(None)
                    else:
                        if i == 0:
                            colors.append(self.grid[neighbor[0]][neighbor[1]].b_c)
                        elif i == 1:
                            colors.append(self.grid[neighbor[0]][neighbor[1]].l_c)
                        elif i == 2:
                            colors.append(self.grid[neighbor[0]][neighbor[1]].t_c)
                        elif i == 3:
                            colors.append(self.grid[neighbor[0]][neighbor[1]].r_c)

                matching_color_tile = Tile(colors[0], colors[1], colors[2], colors[3])
                correct_tile = None
                for tile in self.tiles:
                    if matching_color_tile.matches(tile):
                        correct_tile = tile
                if correct_tile is not None:
                    self.grid[r][c] = correct_tile

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


pattern = Grid(2,2)
pattern.create()
pattern.print_grid()
