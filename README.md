# Advent of Code 2025

Code for Advent of Code 2025 in Python.

## Setup

1. Install Python 3.9 or higher
2. Install dependencies (if any):
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running Solutions

Run a specific day and part using the CLI:

```bash
python3 main.py <day> <part>
```

Examples:

```bash
python3 main.py 1 1  # Run Day 1, Part 1
python3 main.py 1 2  # Run Day 1, Part 2
python3 main.py 2 1  # Run Day 2, Part 1
```

### Testing

Each day's solution file includes a `test()` function that runs both parts and compares against expected outputs.

Run tests for a specific day:

```bash
python3 solutions/day01.py
```

Or run all tests:

```bash
python3 run_tests.py
```

## Project Structure

```
.
├── main.py              # CLI entry point
├── requirements.txt     # Python dependencies
├── inputs/              # Input files
│   ├── day01.txt       # Day 1 input
│   ├── day02.txt       # Day 2 input
│   └── dayXX.txt       # Day XX input
├── utils/               # Utility functions
│   ├── __init__.py
│   └── file_reader.py  # File reading utilities
└── solutions/           # Day solutions
    ├── __init__.py
    ├── day01.py        # Day 1 solution
    └── day02.py        # Day 2 solution
```

## Adding a New Day

1. Create `solutions/dayXX.py` (where XX is the day number, zero-padded)
2. Implement `part1()` and `part2()` functions that return integers
3. Add a `test()` function with expected values
4. Create `inputs/dayXX.txt` with your input data

## Utilities

The `utils` directory contains helper functions:

- `read_input(day, filename)`: Read input file as a string
- `read_lines(day, filename)`: Read input file as a list of lines
- `read_blocks(day, filename, separator)`: Read input file split into blocks

## CI/CD

GitHub Actions automatically runs all tests on push and pull requests.
