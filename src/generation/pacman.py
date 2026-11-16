"""Pac-Man-style connected maze generator."""
import random
from src.generation.base import MazeGenerator


class PacmanGenerator(MazeGenerator):
    def generate(self, maze):
        # TODO:
        # 1. Build a connected spanning structure (you may reuse PerfectGenerator).
        # 2. Open additional walls between already-connected neighbours to create
        #    at least two independent cycles: mu = E - V + 1 >= 2.
        # 3. Keep all ordinary cells connected.
        # 4. Ensure four corners and centre are open corridors as subject defines.
        # 5. Reduce dead ends, but preserve corridor-width and 42 constraints.
        # 6. Validate after modifications; retry or reject invalid candidates.
        # Use random.Random(maze.seed) for reproducibility.
        raise NotImplementedError


def generate_pacman(maze):
    return PacmanGenerator().generate(maze)
