from grid import *
import graphics

pattern = Grid(10,10)
pattern.create()
print(pattern)
graphics.draw_pattern(pattern.grid)
