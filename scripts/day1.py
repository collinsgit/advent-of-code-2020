from typing import List

from util.data import get_input


def part_1(nums: List[str], total: int = 2020) -> int:
    hash_nums = set(map(int, nums))

    for num in hash_nums:
        if total - num in hash_nums:
            return num * (total - num)


def part_2(nums: List[str], total: int = 2020) -> int:
    hash_nums = set(map(int, nums))

    for num1 in hash_nums:
        for num2 in hash_nums:
            if total - num1 - num2 in hash_nums:
                return num1 * num2 * (total - num1 - num2)


if __name__ == "__main__":
    print(part_2(get_input()))
