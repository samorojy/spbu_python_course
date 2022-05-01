from typing import Callable


def curry_explicit(function: Callable, arity: int) -> Callable:
    """
    :param function: function to curry
    :param arity: int positive value of wanted function arity
    :return: curried function
    """
    if arity < 0:
        raise ValueError("Arity can not be negative number")

    def curried_function(arg=None) -> Callable:
        if arity == 0:
            return function()
        if arity == 1:
            return function(arg)
        return curry_explicit(lambda *args: function(arg, *args), arity - 1)

    return curried_function


def uncurry_explicit(function: Callable, arity: int) -> Callable:
    """
    :param function: function to uncurry
    :param arity: int positive value of wanted function arity
    :return: uncurried function
    """
    if arity < 0:
        raise ValueError("Arity can not be negative number")

    def check_match_arity_args(args):
        if len(args) != arity:
            raise ValueError("Incorrect number of arguments or incorrect arity")

    def uncurried_function(*args) -> Callable:
        check_match_arity_args(args)
        result = function() if arity == 0 else function
        for arg in args:
            result = result(arg)
        return result

    return uncurried_function
