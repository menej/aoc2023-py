def read_input(file_path):
    with open(file_path) as f:
        data = [line.strip("\n") for line in f]
    return data
