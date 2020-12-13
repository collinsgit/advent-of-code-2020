from typing import List, Tuple

from util.data import get_input


def decode_seat(seat_code: str) -> Tuple[int, int]:
    row_str = seat_code[:-3]
    col_str = seat_code[-3:]

    row = int(row_str.replace('F', '0').replace('B', '1'), 2)
    col = int(col_str.replace('L', '0').replace('R', '1'), 2)

    return row, col


def part_1(seat_codes: List[str]) -> int:
    seats = map(decode_seat, seat_codes)
    seat_ids = [row * 8 + col for row, col in seats]
    return max(seat_ids)


def part_2(seat_codes: List[str]) -> int:
    seats = map(decode_seat, seat_codes)
    seat_ids = set([row * 8 + col for row, col in seats])
    for seat_id in range(min(seat_ids), max(seat_ids)):
        if seat_id not in seat_ids and seat_id - 1 in seat_ids and seat_id + 1 in seat_ids:
            return seat_id


if __name__ == "__main__":
    print(part_2(get_input()))