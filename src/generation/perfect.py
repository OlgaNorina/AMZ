"""Perfect maze generator: iterative randomized DFS / recursive backtracking."""
import random
from src.algorithms.neighbors import get_unvisited_neighbors
from src.generation.base import MazeGenerator


class PerfectGenerator(MazeGenerator):
    def generate(self, maze):
        visited = set()

        # - Create random.Random(maze.seed), not global random state.
        rng = random.Random(maze.seed)

        # - Use an explicit stack to avoid Python recursion-depth limits.
        stack = []

        # - TODO: Start at a valid traversable cell; do not carve through reserved 42 cells.
        current_cell = (0, 0)

        visited.add(current_cell)
        stack.append(current_cell)

        while stack:
            x, y = stack[-1]

            # - Choose a random unvisited neighbour, open the shared wall, push it.
            neighbors = get_unvisited_neighbors(maze, x, y, visited)
            if neighbors:
                nx, ny, direction = rng.choice(neighbors)

                maze.open_passage(x, y, direction)

                visited.add((nx, ny))
                stack.append((nx, ny))
            
            else:
                # - Backtrack when no unvisited neighbour remains.
                stack.pop()

       
        # - Ensure every non-pattern cell is visited/reachable.
        expected_cells = {(x,y) for x, y, _ in maze.iter_cells()}
        if visited != expected_cells:
            raise RuntimeError("Maze generation is incomplete")
        
        # raise NotImplementedError


def generate_perfect(maze):
    return PerfectGenerator().generate(maze)
