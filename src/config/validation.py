"""Validate parsed configuration values and cross-field constraints."""

REQUIRED_KEYS = {
    "WIDTH", "HEIGHT", "ENTRY", "EXIT", "OUTPUT_FILE", "PERFECT"
}


def validate_config(config: dict) -> None:
    missing = REQUIRED_KEYS - config.keys()
    if missing:
        raise ValueError(f"Missing config keys: {', '.join(sorted(missing))}")

    # TODO: Validate positive dimensions, coordinate tuple shape and bounds,
    # entry != exit, boolean PERFECT, non-empty output path, and optional keys.
    # Consider minimum dimensions required by the 42 pattern and Pac-Man rules.
    raise NotImplementedError("Complete config semantic validation")
