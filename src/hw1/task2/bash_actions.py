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
