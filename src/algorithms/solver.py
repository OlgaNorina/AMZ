"""Shortest-path solver. BFS is suitable because every move has equal cost."""
from collections import deque
from src.algorithms.neighbors import get_open_neighbors


def find_shortest_path(maze):
    # TODO:
    # - BFS from maze.entry using collections.deque.
    # - Track visited coordinates and parents[child] = parent.
    # - Stop when maze.exit is reached.
    # - Reconstruct and return a list of (x, y), including both endpoints.
    # - Return None if no route exists.
    raise NotImplementedError


def path_to_directions(path):
    # TODO: Convert consecutive coordinate differences into N/E/S/W.
    # Validate that each step is exactly one orthogonal cell.
    # Return a string; a path containing only the start has an empty string.
    raise NotImplementedError
