import functools
from typing import Dict, List

from util.data import get_input


def get_jolt_diffs(jolts: List[int]) -> Dict[int, int]:
    jolts += [0, max(jolts) + 3]
    jolts = sorted(jolts)

    diffs = {}
    for i in range(len(jolts)-1):
        diff = jolts[i+1] - jolts[i]
        diffs[diff] = diffs.get(diff, 0) + 1
    return diffs


def count_jolt_arrangements(jolts: List[int]) -> int:
    # assumes that jolts is sorted in increasing order
    jolts = [0] + jolts

    @functools.lru_cache(1000)
    def count_recursive(i: int, max_jolt=None) -> int:
        if max_jolt is None:
            max_jolt = jolts[i]
        total = 0
        for j in range(max(0, i-3), i):
            if max_jolt - jolts[j] <= 3:
                if jolts[j]:
                    total += count_recursive(j, jolts[j])
                else:
                    total += 1
        return total

    return count_recursive(len(jolts), jolts[-1] + 3)


def part_1(jolts: List[str]) -> int:
    jolt_diffs = get_jolt_diffs(list(map(int, jolts)))
    return jolt_diffs[1] * jolt_diffs[3]


def part_2(jolts: List[str]) -> int:
    return count_jolt_arrangements(sorted(list(map(int, jolts))))


if __name__ == "__main__":
    print(part_2(get_input()))
