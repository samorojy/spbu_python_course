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
                n_lines, n_words, n_bytes = 0, 0, 0
                for line in f:
                    n_lines += 1
                    n_words += len(line.split())
                    n_bytes += len(line.encode("utf-8"))
                total_lines += n_lines
                total_words += n_words
                total_bytes += n_bytes
                print(f"{file_path}: lines = {n_lines}, words = {n_words}, bytes = {n_bytes}")
        except FileNotFoundError:
            print(f"No such file {file_path}")
    if len(file_names) > 1:
        print(f"Total: lines = {total_lines}, words = {total_words}, bytes = {total_bytes}")
