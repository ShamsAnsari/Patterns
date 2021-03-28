import unittest
from grid import *


class TestTile(unittest.TestCase):

    def test_init(self):
        tile = Tile()
        self.assertIsNone(tile.t_c)
        self.assertIsNone(tile.r_c)
        self.assertIsNone(tile.b_c)
        self.assertIsNone(tile.l_c)

        tile = Tile("red", "red", "red", "green")
        self.assertEqual(tile.t_c, "red")
        self.assertEqual(tile.r_c, "red")
        self.assertEqual(tile.b_c, "red")
        self.assertEqual(tile.l_c, "green")

        tile = Tile(None, "red", None, "green")
        self.assertIsNone(tile.t_c)
        self.assertEqual(tile.r_c, "red")
        self.assertIsNone(tile.b_c)
        self.assertEqual(tile.l_c, "green")

    def test_matches(self):
        tile1 = Tile()
        tile2 = Tile()
        self.assertTrue(tile1.matches(tile2))

        tile1 = Tile("red", "red", "red", "green")
        tile2 = Tile("red", "red", "red", "green")
        self.assertTrue(tile1.matches(tile2))

        tile1 = Tile("red", "red", None, "green")
        tile2 = Tile("red", "red", "red", "green")
        self.assertTrue(tile1.matches(tile2))

        tile1 = Tile("red", "red", None, "green")
        tile2 = Tile("red", "red", "red", "green")
        self.assertTrue(tile1.matches(tile2))

        tile1 = Tile("red", "red", None, "green")
        tile2 = Tile("red", "blue", "red", "green")
        self.assertFalse(tile1.matches(tile2))


if __name__ == "__main__":
    unittest.main()
