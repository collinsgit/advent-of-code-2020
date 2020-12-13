import re
from typing import Dict, List, Set, Tuple

from util.data import get_input


RULE_PATTERN = re.compile(r"(\d+ )?([a-z ]+?) bags?")


def parse_rules(rules: List[str]) -> Dict[str, List[Tuple[str, int]]]:
    parsed_rules = {}

    for rule in rules:
        holder_str, contents_str = rule.split("contain")
        holder_m = re.match(RULE_PATTERN, holder_str)

        contents = []
        for m in re.finditer(RULE_PATTERN, contents_str):
            if m.group(1):
                contents.append((m.group(2), int(m.group(1))))

        parsed_rules[holder_m.group(2)] = contents

    return parsed_rules


def get_parent_dict(rule_dict: Dict[str, List[Tuple[str, int]]]) -> Dict[str, Set[str]]:
    parents = {}

    for parent, children in rule_dict.items():
        for child, _ in children:
            if child not in parents:
                parents[child] = set()
            parents[child].add(parent)

    return parents


def find_all_parents(parent_dict: Dict[str, str], bag_type: str) -> Set[str]:
    new_parents = parent_dict.get(bag_type, set())
    all_parents = new_parents.copy()

    while new_parents:
        parents = new_parents
        new_parents = set()
        for parent in parents:
            new_parents.update(parent_dict.get(parent, set()))
        new_parents -= all_parents
        all_parents.update(new_parents)

    return all_parents


def count_bags(parsed_rules: Dict[str, List[Tuple[str, int]]], bag_type: str) -> int:
    return 1 + sum([
        num * count_bags(parsed_rules, sub_type)
        for sub_type, num in parsed_rules[bag_type]
    ])


def part_1(rules: List[str], bag_type: str) -> int:
    parent_dict = get_parent_dict(parse_rules(rules))
    return len(find_all_parents(parent_dict, bag_type))


def part_2(rules: List[str], bag_type: str) -> int:
    parsed_rules = parse_rules(rules)
    return count_bags(parsed_rules, bag_type) - 1


if __name__ == "__main__":
    print(part_2(get_input(), "shiny gold"))
