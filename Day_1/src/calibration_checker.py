import os

from src.utils import sum_all_calibration_values, get_first_and_last_number_from_string

if __name__ == "__main__":
    calibration_values = []
    with open(os.path.join("..", "resources", "input.txt"), "r") as infile:
        for line in infile:
            calibration_values.append(get_first_and_last_number_from_string(line))
    total = sum_all_calibration_values(calibration_values)
