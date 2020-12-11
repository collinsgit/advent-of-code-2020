import re
from typing import List

from util.data import get_input

PASS_PATTERN = re.compile(r"(?P<min>\d+)\-(?P<max>\d+) (?P<letter>\w): (?P<password>\w+)")


def is_valid_1(m: re.Match) -> bool:
    count = 0
    for char in m.group("password"):
        if char == m.group("letter"):
            count += 1
        if count > int(m.group("max")):
            return False
    return count >= int(m.group("min"))


def is_valid_2(m: re.Match) -> bool:
    letter1 = m.group("password")[int(m.group("min"))-1]
    letter2 = m.group("password")[int(m.group("max"))-1]

    if letter1 == letter2:
        return False
    elif letter1 == m.group("letter") or letter2 == m.group("letter"):
        return True
    return False


def part_1(passwords: List[str]) -> int:
    return sum(map(lambda password: is_valid_1(re.match(PASS_PATTERN, password)), passwords))


def part_2(passwords: List[str]) -> int:
    return sum(map(lambda password: is_valid_2(re.match(PASS_PATTERN, password)), passwords))


if __name__ == "__main__":
    print(part_2(get_input()))