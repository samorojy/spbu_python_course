import pytest
from src.hw2.curry import curry_explicit, uncurry_explicit


def test_curry_explict_several_arity():
    function = curry_explicit((lambda x, y, z: f"<{x},{y},{z}>"), 3)
    assert function(123)(456)(562) == "<123,456,562>"

    function2 = curry_explicit((lambda x, y, z: f"<{x},{y},{z}>"), 3)(1)(2)
    assert function2(3) == "<1,2,3>"


def test_curry_explict_zero_arity():
    function = curry_explicit((lambda: "expected value"), 0)
    assert function() == "expected value"


def test_curry_explict_one_arity():
    function = curry_explicit((lambda x: x), 1)
    assert function("expected value") == "expected value"


def test_curry_explict_incorrect_arity():
    with pytest.raises(ValueError):
        curry_explicit((lambda x: x), -1)


def test_uncurry_explict_several_arity():
    function = uncurry_explicit((lambda x: lambda y: lambda z: f"<{x},{y},{z}>"), 3)
    assert function(123, 456, 562) == "<123,456,562>"


def test_uncurry_explict_zero_arity():
    with pytest.raises(ValueError):
        uncurry_explicit((lambda x: lambda y: lambda z: f"<{x},{y},{z}>"), 0)(123, 456, 562)
    function = uncurry_explicit(lambda: "expected value", 0)
    assert function() == "expected value"


def test_uncurry_explict_one_arity():
    function = uncurry_explicit((lambda x: x), 1)
    assert function("expected value") == "expected value"


def test_uncurry_explict_incorrect_arity():
    with pytest.raises(ValueError):
        uncurry_explicit((lambda x: x), -1)

    with pytest.raises(ValueError):
        uncurry_explicit((lambda x: x), 2)(1)


def test_curry_uncurry_explict():
    curried_function = curry_explicit((lambda x, y, z: f"<{x},{y},{z}>"), 3)
    assert curried_function(123)(456)(562) == "<123,456,562>"
    uncurried_function = uncurry_explicit(curried_function, 3)
    assert uncurried_function(123, 456, 562) == "<123,456,562>"
