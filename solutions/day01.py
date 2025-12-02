from utils.file_reader import read_lines


def lock_data() -> (int, int):
    lines = read_lines(1)
    current_position = 50
    pointed_at_zero_count = 0
    wrapped_count = 0
    for line in lines:
        direction = line[0]
        steps = int(line[1:])
        is_zero_before = current_position == 0
        if direction == "L":
            current_position -= steps
        elif direction == "R":
            current_position += steps
        else:
            raise ValueError(f"Invalid direction: {direction}")

        if current_position < 0 and not is_zero_before:
            wrapped_count += 1
        if current_position == 0:
            wrapped_count += 1
        wrapped_count += abs(current_position) // 100
        current_position = current_position % 100
        if current_position == 0:
            pointed_at_zero_count += 1
    return pointed_at_zero_count, wrapped_count


def part1() -> int:
    return lock_data()[0]


def part2() -> int:
    return lock_data()[1]
