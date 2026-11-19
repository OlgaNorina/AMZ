"""Application entry point. Keep orchestration here; algorithms belong in modules."""
import sys

from src.config.parser import load_config
from src.config.validation import validate_config
from src.core.maze import Maze
from src.generation.perfect import generate_perfect
from src.generation.pacman import generate_pacman
from src.algorithms.solver import find_shortest_path
from src.validation.maze_validator import validate_maze
from src.output.exporter import export_maze
from src.output.renderer import render_maze


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python3 -m src.main <config_file>", file=sys.stderr)
        return 2

    try:
        config = load_config(sys.argv[1])
        # validate_config(config)

        maze = Maze(
            width=int(config["WIDTH"]),
            height=int(config["HEIGHT"]),
            entry=config["ENTRY"],
            exit=config["EXIT"],
            seed=config.get("SEED"),
        )

        if config["PERFECT"]:
            generate_perfect(maze)
        else:
            generate_pacman(maze)

        # validate_maze(maze, perfect=config["PERFECT"])
        # path = find_shortest_path(maze)

        # if path is None:
        #     raise RuntimeError("No path exists between entry and exit")

        if config.get("DISPLAY", "NONE") == "ASCII":
            # print(render_maze(maze, path))
            print(render_maze(maze))

        # export_maze(maze, config["OUTPUT_FILE"], path)
        return 0

    except (ValueError, OSError, NotImplementedError, RuntimeError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
