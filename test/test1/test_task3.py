from src.test1.task3 import SafeCall

default_file_name = "log.txt"


def test_safe_call():
    @SafeCall(default_file_name)
    def f(n, *args, **kwargs):
        if n % 2 == 0:
            raise Exception
        return n

    f(2, a="1", b="2")
    f(3, a="5")
    f(4, a="5", b="1")

    assert_list = [
        ["f", "(2,)", "({'a':", "'1',", "'b':", "'2'})", ":Exception"],
        ["f", "(4,)", "({'a':", "'5',", "'b':", "'1'})", ":Exception"],
    ]
    with open(default_file_name) as f:
        lines = f.readlines()

        for index, line in enumerate(lines):
            info = line.split(" ")[2:-1]
            assert assert_list[index] == info
