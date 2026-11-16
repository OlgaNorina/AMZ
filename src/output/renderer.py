"""Human-readable ASCII renderer for debugging only."""
from src.core.directions import NORTH, SOUTH, WEST, EAST


def render_maze(maze, path=None) -> str:
    result = []

    path_cells = set(path) if path else set()

    for y in range(maze.height):
        # TODO 1: Нарисовать верхнюю границу строки.
        # Для каждой клетки проверить NORTH.
        top_line = ""
        for x in range(maze.width):
            cell = maze.get_cell(x, y)
            top_line += "+---" if cell.has_wall(NORTH) else "+   "
        top_line += "+"
        result.append(top_line)

        # TODO 2: Нарисовать содержимое строки.
        # Проверить WEST.
        # Определить символ клетки: S, E, *, пробел.
        middle_line = ""
        for x in range(maze.width):
            cell = maze.get_cell(x, y)
            middle_line += "| " if cell.has_wall(WEST) else "  "
            if (x, y) == maze.entry:
                middle_line += "S "
            elif (x, y) == maze.exit:
                middle_line += "E "
            else:
                middle_line += "* " if (x,y) in path_cells else "  "

        last_cell = maze.get_cell(maze.width - 1, y)
        middle_line += "|" if last_cell.has_wall(EAST) else " "
        result.append(middle_line)

    # TODO 3: Нарисовать нижнюю границу последней строки.
    # Использовать SOUTH.
    bottom_line=""
    for x in range(maze.width):
        y = maze.height - 1
        cell = maze.get_cell(x, y)
        bottom_line += "+---" if cell.has_wall(SOUTH) else "+   "
    bottom_line += "+"
    result.append(bottom_line)

    return "\n".join(result)

# def render_maze(maze, path=None) -> str:
    # TODO: Render walls, entry, exit and optionally the solution path.
    # This representation is NOT the required output-file format.
    # raise NotImplementedError
