import datetime
from functools import update_wrapper
from typing import Callable, List


class Spy:
    def __init__(self, function: Callable):
        self.function = function
        self.logs: List[tuple] = []
        update_wrapper(self, function)

    def __call__(self, *args):
        self.logs.append((datetime.datetime.now(), args))
        return self.function(*args)

    def clear(self):
        self.logs.clear()


def print_usage_statistic(function: Callable):
    if not isinstance(function, Spy):
        raise TypeError("Function must be decorated by @Spy")
    for log in function.logs:
        yield log
