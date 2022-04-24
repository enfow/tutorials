"""numpy vs python list.

References:
    - Ideas from High Performance Python, 2nd edition.
    - line_profiler: https://github.com/pyutils/line_profiler

How to run:
    - `$ python numpy_vs_list.py`

Profiling result:

	Timer unit: 1e-06 s

	Total time: 0.007564 s
	File: numpy_vs_list.py
	Function: for_iteration at line 20

	Line #      Hits         Time  Per Hit   % Time  Line Contents
	==============================================================
		20                                           @profile
		21                                           def for_iteration() -> List[List[int]]:
		22                                               """Make zeros with for iteration."""
		23         1          4.0      4.0      0.1      all_zero = list()
		24       101         33.0      0.3      0.4      for _ in range(100):
		25       100         36.0      0.4      0.5          all_zero.append([])
		26     10100       3154.0      0.3     41.7          for _ in range(100):
		27     10000       4337.0      0.4     57.3              all_zero[-1].append(0)
		28         1          0.0      0.0      0.0      return all_zero

	Total time: 0.00105 s
	File: numpy_vs_list.py
	Function: list_comprehension at line 32

	Line #      Hits         Time  Per Hit   % Time  Line Contents
	==============================================================
		32                                           @profile
		33                                           def list_comprehension() -> List[List[int]]:
		34                                               """Make zeros with list comprehension."""
		35         1       1049.0   1049.0     99.9      all_zero = [[0 for _ in range(100)] for _ in range(100)]
		36         1          1.0      1.0      0.1      return all_zero

	Total time: 1.1e-05 s
	File: numpy_vs_list.py
	Function: numpy_zeros at line 40

	Line #      Hits         Time  Per Hit   % Time  Line Contents
	==============================================================
		40                                           @profile
		41                                           def numpy_zeros() -> np.ndarray:
		42                                               """Make zeros with numpy array."""
		43         1         10.0     10.0     90.9      all_zero = np.zeros((100, 100))
		44         1          1.0      1.0      9.1      return all_zero
"""


import numpy as np
from typing import List
import line_profiler

profile = line_profiler.LineProfiler()


# Create (100, 100) all zero array
# for iteration
@profile
def for_iteration() -> List[List[int]]:
    """Make zeros with for iteration."""
    all_zero = list()
    for _ in range(100):
        all_zero.append([])
        for _ in range(100):
            all_zero[-1].append(0)
    return all_zero


# list comprehension
@profile
def list_comprehension() -> List[List[int]]:
    """Make zeros with list comprehension."""
    all_zero = [[0 for _ in range(100)] for _ in range(100)]
    return all_zero


# numpy zeros
@profile
def numpy_zeros() -> np.ndarray:
    """Make zeros with numpy array."""
    all_zero = np.zeros((100, 100))
    return all_zero


if __name__ == "__main__":
    for_iteration()
    list_comprehension()
    numpy_zeros()
    # print profiling results
    profile.print_stats()
