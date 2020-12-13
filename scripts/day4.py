import re
from typing import List, Set, Dict

from util.data import get_input


def check_height(hgt: str) -> bool:
    m = re.fullmatch(re.compile(r"([0-9]+)(in|cm)"), hgt)
    if not m:
        return False
    if m.group(2) == "in":
        return 59 <= int(m.group(1)) <= 76
    else:
        return 150 <= int(m.group(1)) <= 193


def year_in_range(begin: int, end: int):
    def check_year(yr: str):
        m = re.fullmatch(re.compile(r"[0-9]{4}"), yr)
        if not m:
            return False
        return begin <= int(yr) <= end
    return check_year


REQUIRED_FIELDS = {
    "byr": lambda x: year_in_range(1920, 2002)(x),
    "iyr": lambda x: year_in_range(2010, 2020)(x),
    "eyr": lambda x: year_in_range(2020, 2030)(x),
    "hgt": check_height,
    "hcl": lambda x: re.fullmatch(re.compile(r"#[0-9a-f]{6}"), x) is not None,
    "ecl": lambda x: x in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"},
    "pid": lambda x: re.fullmatch(re.compile(r"[0-9]{9}"), x) is not None,
}
OPTIONAL_FIELDS = {
    "cid"
}


def organize_passports(data: List[str]) -> List[Dict[str, str]]:
    passports = []

    passport = dict()
    for datum in data:
        if not datum:
            passports.append(passport)
            passport = dict()
        else:
            fields = datum.split()
            for field in fields:
                key, value = field.split(":")
                passport[key] = value

    if passport:
        passports.append(passport)
    return passports


def is_valid(passport: Set[str]) -> bool:
    if REQUIRED_FIELDS.keys() - passport:
        return False
    if passport - REQUIRED_FIELDS.keys() - OPTIONAL_FIELDS:
        return False
    return True


def is_valid_2(passport: Dict[str, str]) -> bool:
    if not is_valid(set(passport.keys())):
        return False
    return all([
        REQUIRED_FIELDS[key](value)
        if key in REQUIRED_FIELDS else True
        for key, value in passport.items()
    ])


def part_1(data: List[str]) -> int:
    passports = organize_passports(data)
    return sum(map(is_valid, passports))


def part_2(data: List[str]) -> int:
    passports = organize_passports(data)
    return sum(map(is_valid_2, passports))


if __name__ == "__main__":
    print(part_2(get_input()))
