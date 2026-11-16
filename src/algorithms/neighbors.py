"""Neighbour helpers shared by generation and solving."""
from src.core.directions import DIRECTIONS


def get_unvisited_neighbors(maze, x: int, y: int, visited: set):
    # TODO: Return in-bounds traversable neighbours not in visited.
    # Return enough information to open the matching wall (e.g. (nx, ny, direction)).
    neighbors = []

    for direction, direction_data in DIRECTIONS.items():
        dx, dy = direction_data[:2]
        
        nx = x + dx
        ny = y + dy

        if not maze.in_bounds(nx, ny):
            continue

        if (nx, ny) in visited:
            continue

        neighbors.append((nx, ny, direction))

    return neighbors
    # raise NotImplementedError


def get_open_neighbors(maze, x: int, y: int):
    # TODO: Return neighbours reachable through an OPEN wall.
    # Check bounds and the current cell's corresponding wall bit.
    raise NotImplementedError
