from handle_input import read_input


def calibration(cal_doc):
    cal_sum = 0

    for cal_line in cal_doc:
        length = len(cal_line)
        left = None
        right = None

        for i in range(length):
            if cal_line[i].isnumeric():
                left = cal_line[i]
                break

        for i in range(length - 1, -1, -1):
            if cal_line[i].isnumeric():
                right = cal_line[i]
                break

        cal_sum += int(left + right)
    return cal_sum


print(calibration(read_input("input.txt")))
