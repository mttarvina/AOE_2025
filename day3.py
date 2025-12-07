# ******************************************************************************
# benchmarks:
#   - part1 = 0.0033876001834869385 seconds
#   - part2 = 0.00471000000834465 seconds
#
# ******************************************************************************

import time

# INPUT_FILE = "test_input.txt"
INPUT_FILE = "day3_input.txt"

# NUM_DIGITS = 2  # PART 1
NUM_DIGITS = 12 # PART 2

battery_banks: list = []

def find_max_digit(digits_str: str, start_index: int, stop_index: int) -> tuple:
    max_index = -1
    max_digit = "0"
    index = start_index   
    for digit in digits_str[start_index:stop_index]:
        if int(digit) > int(max_digit):
            max_digit = digit
            max_index = index
        index += 1
    return (max_digit, max_index)


def determine_max_number(digits_str: str, size: int) -> int:
    largest_digits: str = ""
    length = len(digits_str)
    start_index = 0
    for i in range(size):
        stop_index = length - size + i + 1                                      # the stop index will only increment by 1
        max_digit, max_index = find_max_digit(digits_str, start_index, stop_index)
        # print(f"max = {max_digit}, idx = {max_index}, start = {start_index}, stop = {stop_index}")
        largest_digits += max_digit
        start_index = max_index + 1                                             # dynamically update start index to
                                                                                #   point to the next digit after the
                                                                                #   previous max digit
    return largest_digits


with open(file=INPUT_FILE, mode="r", encoding="utf-8") as tf:
    battery_banks = tf.read().split()

sum = 0
time_stamp = time.perf_counter()
for battery in battery_banks:
    max_number = int(determine_max_number(battery, NUM_DIGITS)) 
    sum = sum + max_number
    # print(f"{battery} - {max_number}")
print(f"{time.perf_counter() - time_stamp}")
print(f"SUM = {sum}")