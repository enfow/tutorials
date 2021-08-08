"""Example codes for python scope."""

from typing import List


# 1. Inner Function and Outer Function

def call_func() -> None:
    """Call functions."""
    variables = list()

    def inner_func() -> None:
        """Add inner_method string to variables."""
        variables.append("inner_method")

    inner_func()
    variables = outer_func(variables)
    return variables


def outer_func(variables: List[str]) -> None:
    """Add inner_method string to variables."""
    variables.append("outer_method")
    return variables


"""
It raises error with codes below.
Only inner function(nested function) can directly access to the enclosing function's
variables. Althoght the outer function was called inside the enclosing function,
it can not access to them.
"""
# def call_func() -> None:
#    """Call functions."""
#    variables = list()
#
#    def inner_func() -> None:
#        """Add inner_method string to variables."""
#        variables.append("inner_method")
#
#    inner_func()
#    outer_func()
#    return variables
#
#
# def outer_func() -> None:
#    """Add inner_method string to variables."""
#    variables.append("outer_method")

if __name__ == "__main__":
    variables = call_func()
    print(variables)
