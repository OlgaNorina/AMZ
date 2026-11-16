"""Read KEY=VALUE configuration lines. Semantic validation is in validation.py."""
from pathlib import Path


def load_config(filename: str) -> dict:
    config = {}

    with Path(filename).open("r", encoding="utf-8") as file:
        for line_number, raw_line in enumerate(file, start=1):
            line = raw_line.strip()

            if not line or line.startswith("#"):
                continue

            if "=" not in line:
                raise ValueError(f"Line {line_number}: expected KEY=VALUE")

            key, value = (part.strip() for part in line.split("=", 1))
            if not key:
                raise ValueError(f"Line {line_number}: empty key")
            if key in config:
                raise ValueError(f"Line {line_number}: duplicate key {key}")

            config[key] = value

    # TODO: Convert WIDTH/HEIGHT to int, ENTRY/EXIT to (x, y),
    # PERFECT to bool, and SEED to int. Keep parsing errors descriptive.
    # Do not silently accept unknown keys unless the subject permits them.
    return config
