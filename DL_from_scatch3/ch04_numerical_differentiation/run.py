"""Implement numerical differentialtion functions.

Author: Kyeongmin.woo
Email: wgm0601@gmail.com
"""

from typing import Callable
import math


# Numerical Differentiation Functions
def centered_divided_difference(func: Callable[[float], float] , x: float, eps: float = 1e-6) -> float:
    """Define numerical differentialtion with centered divided differentiation.

    Note:
        diff = (f(x + eps) - f(x - eps)) / (2 * eps)
    """
    return (func(x + eps) - func(x - eps)) / (2 * eps)

def forward_divided_difference(func: Callable[[float], float] , x: float, eps: float = 1e-6) -> float:
    """Define numerical differentialtion with forward divided differentiation.

    Note:
        diff = (f(x + eps) - f(x)) / eps
    """
    return (func(x + eps) - func(x)) / eps


# Input Functions
def quadratic(x: float) -> float:
    """Define y = x^2."""
    return x * x

def exponential(x: float) -> float:
    """Define y = e^x."""
    return math.exp(x)


if __name__ == "__main__":
    # Diff between cetered divided and forward divided.
    answer = 2.  # y = x^2 's differentiation is always 2.
    centerd_diff = centered_divided_difference(func=quadratic, x=1)
    forward_diff = forward_divided_difference(func=quadratic, x=1)

    print(f"y=x^2 at 1 | Answer: {answer} | Centered Divided: {centerd_diff} | Forward Divided: {forward_diff}")

    answer = math.e  # y = x^2 's differentiation is always 2.
    centerd_diff = centered_divided_difference(func=exponential, x=1)
    forward_diff = forward_divided_difference(func=exponential, x=1)

    print(f"y=e^x at 1 | Answer: {answer} | Centered Divided: {centerd_diff} | Forward Divided: {forward_diff}")

