from typing import Dict, List

from util.data import get_input


def cache_supports_num(cache: Dict[int, int], num: int) -> bool:
    for cached_num in cache:
        if num - cached_num in cache:
            return True
    return False


def find_first_invalid(nums: List[int], preamble_length=25) -> int:
    cache = {}
    for num in nums[:preamble_length]:
        cache[num] = cache.get(num, 0) + 1

    for i, num in enumerate(nums[preamble_length:]):
        if not cache_supports_num(cache, num):
            return num
        else:
            cache[num] = cache.get(num, 0) + 1
            cache[nums[i]] -= 1
            if cache[nums[i]] == 0:
                del cache[nums[i]]

    raise ValueError("No invalid numbers were found.")


def find_contiguous_range(nums: List[int], total: int) -> List[int]:
    i = 0
    j = 0
    range_total = nums[0]

    while range_total != total:
        if range_total < total or i == j:
            j += 1
            range_total += nums[j]
        else:
            range_total -= nums[i]
            i += 1

    return nums[i:j+1]


def part_1(nums: List[str]) -> int:
    return find_first_invalid(list(map(int, nums)))


def part_2(nums: List[str]) -> int:
    nums = list(map(int, nums))
    total = find_first_invalid(nums)
    cont_range = find_contiguous_range(nums, total)
    return min(cont_range) + max(cont_range)


if __name__ == "__main__":
    print(part_2(get_input()))