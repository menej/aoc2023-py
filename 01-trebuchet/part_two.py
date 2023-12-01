from handle_input import read_input

digits = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

first_letter_digits = {x[0] for x in digits.keys()}


def handle_side(i, cal_line):
    length = len(cal_line)
    char = cal_line[i]

    if char.isnumeric():
        return cal_line[i]

    if char in first_letter_digits:
        max_length = length - i

        len_three = cal_line[i:i + 3] if 3 <= max_length else None
        len_four = cal_line[i:i + 4] if 4 <= max_length else None
        len_five = cal_line[i:i + 5] if 5 <= max_length else None

        if len_three is not None or len_four is not None or len_five is not None:
            for digit, value in digits.items():
                if digit in [len_three, len_four, len_five]:
                    return value


def calibration(cal_doc):
    cal_sum = 0

    for cal_line in cal_doc:
        length = len(cal_line)
        left = None
        right = None

        # handle left side
        i = 0
        while i < length and left is None:
            left = handle_side(i, cal_line)
            i += 1

        assert left is not None, "Error in input: left digit was not found"

        # handle right side
        i = length - 1
        while i >= 0 and right is None:
            right = handle_side(i, cal_line)
            i -= 1

        assert right is not None, "Error in input: right digit was not found"

        cal_sum += int(left + right)
    return cal_sum


print(calibration(read_input("input.txt")))
