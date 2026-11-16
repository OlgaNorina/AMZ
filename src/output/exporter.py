"""Serialize the maze in the subject's hexadecimal output format."""
from pathlib import Path
from src.algorithms.solver import path_to_directions


def export_maze(maze, filename: str, path) -> None:
    # TODO:
    # - One uppercase hexadecimal digit per cell, row by row.
    # - One newline after every maze row.
    # - One empty line.
    # - Entry coordinates on their own line.
    # - Exit coordinates on their own line.
    # - Shortest path directions on their own line.
    # - Ensure the final line also ends in '\n'.
    # - Create parent output directory if appropriate.
    # Check exact coordinate notation against the full subject/examples.
    raise NotImplementedError
