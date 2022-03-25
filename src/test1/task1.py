import datetime
from functools import update_wrapper
from typing import Callable, List


class Spy:
    def __init__(self, function: Callable):
        self.function: Callable = function
        self.logs: List = []
        update_wrapper(self, function)

    def __call__(self, *args, **kwargs):
        self.logs.append((datetime.datetime.now(), (args, kwargs)))
        return self.function(*args, **kwargs)

    def clear(self):
        self.logs.clear()


def print_usage_statistic(function: Callable):
    if not isinstance(function, Spy):
        raise TypeError("Function must be decorated by @Spy")
    for log in function.logs:
        yield log