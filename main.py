#!/usr/bin/env python3
"""
Advent of Code 2025 - Main CLI
Usage: python3 main.py <day> <part>
Example: python3 main.py 1 2
"""
import sys
import importlib


def main():
    if len(sys.argv) != 3:
        print("Usage: python3 main.py <day> <part>")
        print("Example: python3 main.py 1 2")
        sys.exit(1)

    try:
        day = int(sys.argv[1])
        part = int(sys.argv[2])
    except ValueError:
        print("Error: Day and part must be integers")
        sys.exit(1)

    if part not in [1, 2]:
        print("Error: Part must be 1 or 2")
        sys.exit(1)

    # Format day as two-digit string (e.g., "01", "02")
    day_str = f"{day:02d}"

    try:
        # Import the day module
        module_name = f"solutions.day{day_str}"
        module = importlib.import_module(module_name)

        # Get the appropriate part function
        part_func = getattr(module, f"part{part}", None)
        if part_func is None:
            print(f"Error: part{part} function not found in {module_name}")
            sys.exit(1)

        # Run the part and print the result
        result = part_func()
        print(result)

    except ImportError as e:
        print(f"Error: Could not import {module_name}")
        print(f"Details: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error running part {part} of day {day}: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
