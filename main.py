from grid import *
import graphics

pattern = Grid(19,19)
pattern.create()
print("Num rows: {}".format(pattern.num_rows))
print("Num cols: {}".format(pattern.num_cols))
for r in range(pattern.num_rows):
    print(pattern.grid[r])

#graphics.draw_pattern(pattern.grid)
