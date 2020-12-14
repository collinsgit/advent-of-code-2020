from typing import List

from util.data import get_input


def accumulate(commands: List[str]) -> int:
    completed = set()
    next = 0
    total = 0

    while next not in completed and next < len(commands):
        completed.add(next)
        command = commands[next].split()
        if command[0] == "acc":
            total += int(command[1])
        elif command[0] == "jmp":
            next += int(command[1])
            continue
        next += 1

    return total


def correct_commands(commands: List[str]) -> List[str]:
    commands = commands.copy()

    forward_dict = {}
    for i, command in enumerate(commands):
        com_type, val = command.split()
        val = int(val)

        if com_type == "jmp":
            forward_dict[i] = i + val
        else:
            forward_dict[i] = i + 1

    backward_dict = {}
    for start, end in forward_dict.items():
        if end not in backward_dict:
            backward_dict[end] = set()
        backward_dict[end].add(start)

    possible_starts = set()
    parents = {len(commands) - 1, }

    while parents:
        new_parents = set()
        for parent in parents:
            new_parents.update(backward_dict.get(parent, set()))
        new_parents -= possible_starts
        possible_starts.update(new_parents)
        parents = new_parents

    completed = set()
    i = 0
    while i not in completed:
        completed.add(i)

        com_type, val = commands[i].split()
        val = int(val)

        if com_type == "jmp":
            if i + 1 in possible_starts:
                commands[i] = f"nop {val}"
                return commands
            i += val
        elif com_type == "nop":
            if i + val in possible_starts:
                commands[i] = f"jmp {val}"
                return commands
            i += 1
        else:
            i += 1

    raise ValueError("This should not happen for a valid input.")


def part_1(commands: List[str]) -> int:
    return accumulate(commands)


def part_2(commands: List[str]) -> int:
    corrected_commands = correct_commands(commands)
    return accumulate(corrected_commands)


if __name__ == "__main__":
    print(part_2(get_input()))
