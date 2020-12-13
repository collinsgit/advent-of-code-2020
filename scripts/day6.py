from string import ascii_lowercase as alphabet
from typing import List, Set

from util.data import get_input


def parse_answers(answers: List[str], all_required=False) -> List[Set[str]]:
    group_responses = []
    true_answers = set(alphabet) if all_required else set()

    for answer in answers:
        if not answer:
            group_responses.append(true_answers)
            true_answers = set(alphabet) if all_required else set()
        else:
            if all_required:
                true_answers = true_answers & set(answer)
            else:
                true_answers = true_answers | set(answer)

    if true_answers:
        group_responses.append(true_answers)
    return group_responses


def part_1(answers: List[str]) -> int:
    parsed_answers = parse_answers(answers)
    return sum(map(len, parsed_answers))


def part_2(answers: List[str]) -> int:
    parsed_answers = parse_answers(answers, True)
    return sum(map(len, parsed_answers))


if __name__ == "__main__":
    print(part_2(get_input()))