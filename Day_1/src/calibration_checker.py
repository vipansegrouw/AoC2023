import os
from typing import List


def get_first_and_last_number_from_string(input_string: str) -> int:
    output_1 = None
    output_2 = None
    for c in input_string:
        if is_a_number(c):
            output_1 = int(c)
            break
    for c in reversed(input_string):
        if is_a_number(c):
            output_2 = int(c)
            break
    if isinstance(output_1, int) and isinstance(output_2, int):
        return output_1 * 10 + output_2
    else:
        raise Exception(f"Did not find two values. Returned {output_1} and {output_2}.")


def is_a_number(character: str) -> bool:
    try:
        int(character)
        return True
    except ValueError:
        return False


def sum_all_calibration_values(values: List[int]) -> int:
    total = 0
    for input_pair in values:
        total += input_pair
    return total


if __name__ == "__main__":
    calibration_values = []
    with open(os.path.join("..", "resources", "input.txt"), "r") as infile:
        for line in infile:
            calibration_values.append(get_first_and_last_number_from_string(line))
    total = sum_all_calibration_values(calibration_values)
    print(total)

