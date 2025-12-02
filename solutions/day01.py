"""
Advent of Code 2025 - Day 1
"""
from utils.file_reader import read_lines


def part1() -> int:
    """
    Part 1 solution for Day 1

    Returns:
        The result for part 1
    """
    lines = read_lines(1)
    # TODO: Implement part 1
    return 0


def part2() -> int:
    """
    Part 2 solution for Day 1

    Returns:
        The result for part 2
    """
    lines = read_lines(1)
    # TODO: Implement part 2
    return 0


def test():
    """
    Test suite for Day 1
    Runs both parts and compares against expected output
    """
    expected_part1 = None  # TODO: Set expected value
    expected_part2 = None  # TODO: Set expected value

    result_part1 = part1()
    result_part2 = part2()

    print(f"Day 1 - Part 1: {result_part1} (expected: {expected_part1})")
    print(f"Day 1 - Part 2: {result_part2} (expected: {expected_part2})")

    if expected_part1 is not None and result_part1 != expected_part1:
        raise AssertionError(
            f"Part 1 failed: got {result_part1}, expected {expected_part1}")

    if expected_part2 is not None and result_part2 != expected_part2:
        raise AssertionError(
            f"Part 2 failed: got {result_part2}, expected {expected_part2}")

    print("Day 1: All tests passed!")


if __name__ == "__main__":
    test()
