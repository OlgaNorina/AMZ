"""Top-level maze validation; keep individual checks in focused modules."""


def validate_maze(maze, perfect: bool) -> None:
    # TODO: Call focused checks:
    # - entry/exit are distinct and in bounds;
    # - external borders are closed;
    # - neighbouring wall bits are symmetric;
    # - every ordinary cell is connected (42 cells are the specified exception);
    # - no forbidden 3x3 open area / corridor width violation;
    # - 42 pattern is present and made of fully closed cells;
    # - perfect: connected graph has E == V - 1;
    # - pacman: connected graph has E - V + 1 >= 2, corners/centre open,
    #   and dead-end count is within the chosen interpretation of the subject.
    raise NotImplementedError
