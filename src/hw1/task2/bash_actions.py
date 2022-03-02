def head(file_name: str, n: int = 10):
    try:
        with open(file_name) as f:
            for i, line in enumerate(f):
                if i == n:
                    break
                print(line.rstrip())
    except FileNotFoundError:
        print(f"No such file {file_name}")


def tail(file_name: str, n: int = 10):
    try:
        with open(file_name) as f:
            reversed_lines = list(reversed(f.readlines()))
            print("".join(list(reversed(reversed_lines[:n]))))
    except FileNotFoundError:
        print(f"No such file {file_name}")


def nl(*file_names: str):
    for file_path in file_names:
        if len(file_names) > 1:
            print(f"\t\t{file_path}")
        try:
            with open(file_path) as f:
                counter = 1
                for line in f:
                    if not line.isspace():
                        print(f"{counter}.\t{line.rstrip()}")
                        counter += 1
                    else:
                        print(line.rstrip())
        except FileNotFoundError:
            print(f"No such file {file_path}")


def wc(*file_names: str):
    total_lines, total_words, total_bytes = 0, 0, 0
    for file_path in file_names:
        try:
            with open(file_path) as f:
                lines_number, words_number, bytes_number = 0, 0, 0
                for line in f:
                    lines_number += 1
                    words_number += len(line.split())
                    bytes_number += len(line.encode("utf-8"))
                total_lines += lines_number
                total_words += words_number
                total_bytes += bytes_number
                print(f"{file_path}: lines = {lines_number}, words = {words_number}, bytes = {bytes_number}")
        except FileNotFoundError:
            print(f"No such file {file_path}")
    if len(file_names) > 1:
        print(f"Total: lines = {total_lines}, words = {total_words}, bytes = {total_bytes}")
