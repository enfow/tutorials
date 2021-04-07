"""Example of python debugger pdb.

Owner: Kyeongmin Woo
Email: wgm0601@gmail.com

References:
    - pdb-The Python Debugger: https://docs.python.org/3/library/pdb.html

Useful Command for pdb Prompter:
    - s(tep): go to next line
    - n(ext): go to next line(same as step)
    - c(ontinue): pass all lines until the breakpoint
    - r(eturn): pass all lines until the return of the current function
    - where : show current line

    - l(ist): show source code of current function
    - source [function_name]: show source code of the input function_name

    - up: move the current frame count level up in the stack trace
    - down: move the current frame count level down in the stack trace

    - break [statement]: show breakpoints and it's number in the statement
    - disable [breakpoint_number]: disable certain breakpoint
    - enable [breakpoint_number]: enable certain breakpoint

    - p [expression]: evaluate the expression with the current context
"""
import pdb


def breakpoint_with_set_trace(value: int) -> int:
    """Add one breakpoint with pdb.set_trace."""
    a = 10
    b = 20
    pdb.set_trace()
    c = 30
    return a + b + c + value


def breakpoint_with_breakpoint(value: int) -> int:
    """Add one breakpoint with breakpoint().

    Notes:
        you can use breakpoint() with python version 3.7+
    """
    a = 10
    b = 20
    breakpoint()
    c = 30
    breakpoint()
    return a + b + c + value


if __name__ == "__main__":
    breakpoint_with_breakpoint(100)
