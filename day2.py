from typing import List, Tuple

INPUT_FILE: str = "day2_input.txt"
# INPUT_FILE: str = "test_input.txt"


def split_equal_parts(input_str: str, parts: int):
    str_parts: List[str] = []
    if len(input_str) % parts == 0:
        start = 0
        str_len = len(input_str) // parts
        for i in range(parts):
            start = i*str_len
            end = (i+1)*str_len
            str_parts.append(input_str[start:end])
    return str_parts


range_list: List[Tuple[str, str]] = []
with open(file=INPUT_FILE, mode="r", encoding="utf-8") as tf:
    tmp = tf.read().split(",")
    for line in tmp:
        tmp_range = line.split("-")
        range_list.append((tmp_range[0], tmp_range[1]))

invalid_ids: List[int] = []

# # ******************************************************************************
# # PART 1
# for range_item in range_list:
#     for number in range(int(range_item[0]), int(range_item[1]) + 1):
#         num_str = str(number)
        
#         # num_str has even characters
#         if len(num_str) % 2 == 0:
#             mid_index = len(num_str) // 2

#             left_str = num_str[:mid_index]
#             right_str = num_str[mid_index:]

#             if left_str == right_str:
#                 invalid_ids.append(number)

# sum = 0
# for _id in invalid_ids:
#     print(_id)
#     sum += _id
# print(f"SUM = {sum}")
# # END OF PART 1
# # ******************************************************************************

# ******************************************************************************
# PART 2
for range_item in range_list:
    for number in range(int(range_item[0]), int(range_item[1]) + 1):
        num_str = str(number)
        for grouping in range(1, len(num_str) + 1):
            str_parts = split_equal_parts(num_str, grouping)
            if len(str_parts) > 1 and len(set(str_parts)) == 1:
                print(f"{str_parts} - Invalid")
                invalid_ids.append(number)
                break
            else:
                # print(f"{str_parts}")
                continue

sum = 0
for _id in invalid_ids:
    print(_id)
    sum += _id
print(f"SUM = {sum}")
# END OF PART 2
# ******************************************************************************