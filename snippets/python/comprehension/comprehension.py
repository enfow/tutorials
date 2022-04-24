"""Examples for python list comprehensions."""

from typing import List


def get_0_to_9() -> List[int]:
    """Get list of integers from 0 to 9."""
    ret = [num for num in range(10)]
    return ret


def get_product_of_0_to_5() -> List[int]:
    """Get list of integers from 0 to 19 with double for iterations."""
    ret = [(num1, num2) for num1 in range(5) for num2 in range(5)]
    return ret


def get_product_of_0_to_5_first_one_is_bigger_then_second() -> List[int]:
    """Get list of integers from 0 to 19 with double for iterations."""
    ret = [(num1, num2) for num1 in range(5) for num2 in range(num1)]
    return ret


"""It raises error with function below.
In list comprehension, it looks like that the first for iteration nests the next ones.
"""
# def get_product_of_0_to_5_second_one_is_bigger_then_first() -> List[int]:
#    """Get list of integers from 0 to 19 with double for iterations."""
#    ret = [(num1, num2) for num1 in range(num2) for num2 in range(5)]
#    return ret


if __name__ == "__main__":
    print(get_0_to_9())
    print(get_product_of_0_to_5())
    print(get_product_of_0_to_5_first_one_is_bigger_then_second())
