from grid import *
import graphics

pattern = Grid(3,3)
pattern.fill(0,0)
print(pattern)
graphics.draw_pattern(pattern.grid)
