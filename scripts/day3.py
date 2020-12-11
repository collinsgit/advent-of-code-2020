from functools import reduce
from typing import List

from util.data import get_input


def traverse(lines: List[str], rise: int, run: int) -> int:
    line_len = len(lines[0])
    row, col = (0, 0)

    count = 0
    while row < len(lines):
        if lines[row][col] == "#":
            count += 1

        row += rise
        col = (col + run) % line_len

    return count


def part_1(lines: List[str]) -> int:
    return traverse(lines, 1, 3)


def part_2(lines: List[str]) -> int:
    return reduce(
        lambda x, y: x * y,
        [
            traverse(lines, rise, run)
            for rise, run in
            [
                (1, 1),
                (1, 3),
                (1, 5),
                (1, 7),
                (2, 1),
            ]
        ]
    )


if __name__ == "__main__":
    print(part_2(get_input()))
