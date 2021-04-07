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


def example_function(value: int) -> int:
    """Define simple code example."""
    a = 10
    b = 20
    c = 30
    return a + b + c + value


if __name__ == "__main__":
    # Pass statement to pdb.run as string.
    # With this code, you can enter the (pdb) prompter.
    # In the (pdb) promter, use pdb commands.
    pdb.run("example_function(10)")
