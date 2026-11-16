"""Common generator contract; generators mutate the supplied Maze."""
from abc import ABC, abstractmethod


class MazeGenerator(ABC):
    @abstractmethod
    def generate(self, maze):
        """Generate passages in maze. Use a local random.Random(maze.seed)."""
        raise NotImplementedError
