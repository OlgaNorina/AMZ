"""In-memory maze model. Coordinates are always (x, y); grid access is grid[y][x]."""
from src.core.cell import Cell
from src.core.directions import DIRECTIONS


class Maze:
    def __init__(self, width: int, height: int, entry: tuple,
                 exit: tuple, seed: int | None = None):
        self.width = width
        self.height = height
        self.entry = entry
        self.exit = exit
        self.seed = seed
        self.grid = [
            [Cell() for _ in range(width)]
            for _ in range(height)
        ]

    def in_bounds(self, x: int, y: int) -> bool:
        return 0 <= x < self.width and 0 <= y < self.height

    def get_cell(self, x: int, y: int) -> Cell:
        if not self.in_bounds(x, y):
            raise IndexError(f"Cell out of bounds: ({x}, {y})")
        return self.grid[y][x]

    def open_passage(self, x: int, y: int, direction: str) -> None:
        if direction not in DIRECTIONS:
            raise ValueError(f"Invalid direction: {direction}")
        
        # 1. Look up dx, dy and both wall bits in DIRECTIONS.
        dir_data = DIRECTIONS[direction]
        dx = dir_data[0]
        dy = dir_data[1]

        # 2. Calculate neighbour coordinates and reject out-of-bounds moves.
        nx = x + dx
        ny = y + dy
        
        if not self.in_bounds(nx, ny):
            raise ValueError("Cannot open passage outside maze boundaries")
        
        current_cell = self.get_cell(x, y)
        neighbour_cell = self.get_cell(nx, ny)

        # 3. Open the wall in this cell AND the opposite wall in the neighbour.
        current_wall_bit = dir_data[2]
        current_cell.walls &= ~current_wall_bit

        neighbour_wall_bit = dir_data[3]
        neighbour_cell.walls &= ~neighbour_wall_bit

        # 4. Never create asymmetric walls.
        # raise NotImplementedError

    def iter_cells(self):
        """Yield (x, y, Cell) row by row."""
        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                yield x, y, cell
