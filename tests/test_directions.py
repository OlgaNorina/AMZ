import unittest

from src.core.directions import NORTH, EAST, SOUTH, WEST
from src.core.cell import Cell


class TestDirections(unittest.TestCase):
    def test_bit_values_match_subject(self):
        self.assertEqual((NORTH, EAST, SOUTH, WEST), (1, 2, 4, 8))

    def test_hexadecimal_encoding(self):
        self.assertEqual(Cell(walls=0b1010).to_hex(), "A")
        self.assertEqual(Cell(walls=0b0011).to_hex(), "3")


if __name__ == "__main__":
    unittest.main()
