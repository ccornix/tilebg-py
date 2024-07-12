"""Custom higher-order functions.

Extension of the `functools` module of the Python Standard Library.

"""

__author__ = "ccornix"
__copyright__ = "Copyright (c) 2024 ccornix"
__license__ = "MIT"
__all__ = ["repeated"]

from collections.abc import Callable
from functools import reduce


def repeated(f: Callable, n: int, *args) -> Callable:
    """Return a function that apply a callable `f` `n`-times."""

    def repfunc(x):
        return reduce(lambda y, _: f(y, *args), range(n), x)

    return repfunc
