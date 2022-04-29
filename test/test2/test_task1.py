from src.test2.task1 import Logger

default_file_name = "log.txt"


def test_logger():
    @Logger(default_file_name)
    def f(n, *args, **kwargs):
        if n != 0:
            f(n - 1)

    f(1, a="1", b="2")

    assert_list = [
        ["f", "(0,)", "({})", "None"],
        ["f", "(1,)", "({'a':", "'1',", "'b':", "'2'})", "None"],
    ]
    with open(default_file_name) as f:
        lines = f.readlines()[:-1]
        for index, line in enumerate(lines):
            info = line.split(" ")[2:-1]
            assert assert_list[index] == info
