from typing import List

# INPUT_FILE: str = "test_input.txt"
INPUT_FILE: str = "day1_input.txt"
STARTING_POSITION = 50

input_codes: List[str] = []
with open(file=INPUT_FILE, mode="r", encoding="utf-8") as tf:
    input_codes = tf.read().split()

password: int = 0
current_position = STARTING_POSITION
for code in input_codes:
    # print(code)
    full_rotation = int(code[1:]) // 100
    excess_rotation = int(code[1:]) % 100

    password += full_rotation

    if "R" in code:
        tmp = current_position + excess_rotation
    elif "L" in code:
        tmp = current_position - excess_rotation

    if current_position > 0 and (tmp < 0 or tmp > 100):
        password += 1
    
    if tmp > 100:
        current_position = tmp - 100
    elif tmp < 0:
        current_position = tmp + 100
    elif tmp == 100:
        current_position = 0
    else:
        current_position = tmp

    if current_position == 0:
        password += 1

print(password)