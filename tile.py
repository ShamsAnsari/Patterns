class Tile:
    def __init__(self, top_color=None, right_color=None, bottom_color=None, left_color=None):
        self.t_c = top_color
        self.r_c = right_color
        self.b_c = bottom_color
        self.l_c = left_color

    def matches_section(self, color1, color2):
        if color1 is None or color2 is None:
            return True
        if color1.lower() == color2.lower():
            return True
        return False

    def matches(self, tile):
        return (self.matches_section(self.t_c, tile.t_c) and self.matches_section(self.r_c, tile.r_c)
            and self.matches_section(self.b_c, tile.b_c) and self.matches_section(self.l_c, tile.l_c))



    def __repr__(self):
        return "t_c: {}, r_c: {}, b_c: {}, l_c: {}".format(self.t_c, self.r_c, self.b_c, self.l_c)

    def __str__(self):
        return self.__repr__()
