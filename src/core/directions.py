"""Direction constants shared by the model and algorithms."""

NORTH = 0b0001
EAST = 0b0010
SOUTH = 0b0100
WEST = 0b1000

# (dx, dy, current-cell wall bit, neighbour's opposite wall bit)
DIRECTIONS = {
    "N": (0, -1, NORTH, SOUTH),
    "E": (1, 0, EAST, WEST),
    "S": (0, 1, SOUTH, NORTH),
    "W": (-1, 0, WEST, EAST),
}

ALL_WALLS = NORTH | EAST | SOUTH | WEST
