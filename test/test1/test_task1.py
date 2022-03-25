import pytest

from src.test1.task1 import Spy, print_usage_statistic


def test_spy_decorator():
    @Spy
    def foo(*nums):
        print(nums)

    @Spy
    def is_even(num):
        return num % 2 == 0

    foo(1, 2, 3)
    foo(4, 5)
    foo_args = [args for (time, args) in print_usage_statistic(foo)]
    assert foo_args[0] == ((1, 2, 3), {})
    assert foo_args[1] == ((4, 5), {})

    is_even(6)
    is_even(3)
    is_even_args = [args for (time, args) in print_usage_statistic(is_even)]
    assert is_even_args[0] == ((6,), {})
    assert is_even_args[1] == ((3,), {})

    def print_hi():
        print("hi")

    print_hi()
    with pytest.raises(TypeError):
        args = [args for (time, args) in print_usage_statistic(print_hi)]
