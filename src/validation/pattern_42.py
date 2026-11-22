"""Reservation and validation of the fully closed-cell '42' pattern."""

def get_pattern_mask(width: int, height: int) -> set:
    # TODO: Return coordinates reserved for the digits 4 and 2.
    # Decide placement and scale from the full subject / evaluator expectations.
    pattern = [
        [1, 0, 0, ' ', 1, 1, 1],
        [1, 0, 0, ' ', 0, 0, 1],
        [1, 1, 1, ' ', 1, 1, 1],
        [0, 0, 1, ' ', 1, 0, 0],
        [0, 0, 1, ' ', 1, 1, 1]
    ]
    p_w = len(pattern[0])
    p_h = len(pattern)

    start_x = (width - p_w) // 2
    start_y = (height - p_h) // 2

    mask_coordinates = set()

    for dy in range(p_h):
        for dx in range(p_w):
            if pattern[dy][dx] == 1:
                mask_coordinates.add((start_x + dx, start_y + dy))
                
    return mask_coordinates
    #raise NotImplementedError


def validate_pattern_42(maze) -> bool:
    # TODO: Check that every mask cell exists and has all four walls closed.
    mask = get_pattern_mask(maze.width, maze.height)
    
    for x, y in mask:
        if not maze.is_valid_cell(x, y):
            return False
        for direction in ['NORTH', 'SOUTH', 'EAST', 'WEST']:
            if not maze.has_wall(x, y, direction):
                return False

    return True
    #raise NotImplementedError
