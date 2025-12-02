from pathlib import Path


def read_input(day: int) -> str:
    day_str = f"{day:02d}"
    filename = f"day{day_str}.txt"

    file_path = Path(__file__).parent.parent / "inputs" / filename

    if not file_path.exists():
        raise FileNotFoundError(f"Input file not found: {file_path}")

    with open(file_path, "r") as f:
        return f.read()


def read_lines(day: int, strip: bool = True) -> list[str]:
    content = read_input(day)
    lines = content.splitlines()
    if strip:
        lines = [line.strip() for line in lines]
    return lines


def read_blocks(day: int, separator: str = "\n\n") -> list[str]:
    content = read_input(day)
    return content.split(separator)
