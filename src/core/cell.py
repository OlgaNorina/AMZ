"""One maze cell. A set bit means that the corresponding wall is closed."""
from dataclasses import dataclass
from src.core.directions import ALL_WALLS


@dataclass
class Cell:
    walls: int = ALL_WALLS

    def has_wall(self, wall_bit: int) -> bool:
        return bool(self.walls & wall_bit)

    def open_wall(self, wall_bit: int) -> None:
        # TODO: Validate that wall_bit is one of the four supported bits.
        self.walls &= ~wall_bit

    def close_wall(self, wall_bit: int) -> None:
        # TODO: Validate that wall_bit is one of the four supported bits.
        self.walls |= wall_bit

    def to_hex(self) -> str:
        # Subject requires exactly one hexadecimal digit per cell.
        return format(self.walls, "X")
