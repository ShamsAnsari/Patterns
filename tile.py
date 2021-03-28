class Tile:
    def __init__(self, top_color=None, right_color=None, bottom_color=None, left_color=None):
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

