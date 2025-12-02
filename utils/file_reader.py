"""
File reading utilities for Advent of Code
"""
from pathlib import Path


def read_input(day: int, filename: str = None) -> str:
    """
    Read input file for a given day.

    Args:
        day: The day number (1-25)
        filename: The name of the input file (default: None, uses dayXX.txt)

    Returns:
        The contents of the file as a string
    """
    day_str = f"{day:02d}"
    if filename is None:
        filename = f"day{day_str}.txt"

    file_path = Path(__file__).parent.parent / "inputs" / filename

    if not file_path.exists():
        raise FileNotFoundError(f"Input file not found: {file_path}")

    with open(file_path, "r") as f:
        return f.read()


def read_lines(day: int, filename: str = None, strip: bool = True) -> list[str]:
    """
    Read input file and return as a list of lines.

    Args:
        day: The day number (1-25)
        filename: The name of the input file (default: None, uses dayXX.txt)
        strip: Whether to strip whitespace from each line (default: True)

    Returns:
        A list of lines from the file
    """
    content = read_input(day, filename)
    lines = content.splitlines()
    if strip:
        lines = [line.strip() for line in lines]
    return lines


def read_blocks(day: int, filename: str = None, separator: str = "\n\n") -> list[str]:
    """
    Read input file and split into blocks separated by the given separator.

    Args:
        day: The day number (1-25)
        filename: The name of the input file (default: None, uses dayXX.txt)
        separator: The separator between blocks (default: double newline)

    Returns:
        A list of blocks (strings)
    """
    content = read_input(day, filename)
    return content.split(separator)
