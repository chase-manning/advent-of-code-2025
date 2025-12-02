#!/usr/bin/env python3
import sys
import importlib
from pathlib import Path
from solutions.day01 import part1 as day01_part1, part2 as day01_part2
from solutions.day02 import part1 as day02_part1, part2 as day02_part2


def run_test(day: int, part: int, actual: int, expected: int):
    padded_day = f"{day:02d}"
    padded_part = f"{part:02d}"

    if expected != actual:
        print(
            f"Day {padded_day}, Part {padded_part}: Expected {expected}, got {actual} ❌")
        return False
    else:
        print(f"Day {padded_day}, Part {padded_part} passed ✅")
        return True


def run_all_tests():
    tests_passed = True
    tests_passed &= run_test(1, 1, day01_part1(), 0)
    tests_passed &= run_test(1, 2, day01_part2(), 0)
    tests_passed &= run_test(2, 1, day02_part1(), 0)
    tests_passed &= run_test(2, 2, day02_part2(), 0)
    if tests_passed:
        print("\n")
        print("All tests passed ✅")
    else:
        print("\n")
        print("Some tests failed ❌")
        sys.exit(1)


if __name__ == "__main__":
    run_all_tests()
