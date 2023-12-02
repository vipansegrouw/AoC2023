from typing import List

import regex as re


def get_first_and_last_number_from_string(input_string: str) -> int:
    expression = "(one|two|three|four|five|six|seven|eight|nine|zero|1|2|3|4|5|6|7|8|9|0)"
    matches = re.findall(expression, input_string, overlapped=True)
    if matches:
        print(matches)
        first = string_to_number(matches[0])
        last = string_to_number(matches[-1])
        return first*10+last
    else:
        raise Exception("There were no calibration numbers found")


def string_to_number(string: str) -> int:
    dictionary = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "zero": 0,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "0": 0
    }
    return dictionary[string]


def sum_all_calibration_values(values: List[int]) -> int:
    total = 0
    for input_pair in values:
        total += input_pair
    return total
