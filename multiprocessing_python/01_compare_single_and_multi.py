"""Compare single process and multi process.

Author: Kyeongmin Woo
Email: wgm0601@gmail.com
"""
import os
import argparse
from typing import Dict, List
import time
import multiprocessing as mp

import matplotlib.pyplot as plt

# type alias`
N_ITER = int
N_TASK = int
EXEC_TIME = float
RESULTS = Dict[N_TASK, Dict[str, List[EXEC_TIME]]]

# argment parser
parser = argparse.ArgumentParser()
parser.add_argument("--n_iters", nargs="+", default=[100], type=int)
parser.add_argument("--n_tasks", nargs="+", default=[1, 2, 3, 4, 5, 6, 7, 8], type=int)
args = parser.parse_args()

# global variables
SAVE_DIR = os.path.join("img", "compare_single_and_multi")
N_ITERS = args.n_iters
N_TASKS = args.n_tasks

# task
def double_for_iteration(n: int = 100) -> None:
    """Run double for iteration."""
    for _ in range(n):
        for _ in range(n):
            pass


# set multiprocess setting as fork
mp.set_start_method("fork")

# run
results: RESULTS = dict()
for n_task in N_TASKS:

    result_table: Dict[str, List[EXEC_TIME]] = {
        "single": list(),
        "multi": list(),
    }

    for n in N_ITERS:

        # run single process
        start_single_p = time.time()

        for task in range(n_task):
            double_for_iteration(n=n)

        finish_single_p = time.time()
        single_exec_time = round(finish_single_p - start_single_p, 5)

        # run multi process
        start_multi_p = time.time()

        with mp.Pool(n_task) as p:
            p.map(double_for_iteration, [n for _ in range(n_task)])

        finish_multi_p = time.time()
        multi_exec_time = round(finish_multi_p - start_multi_p, 5)

        # log table
        result_table["single"].append(single_exec_time)
        result_table["multi"].append(multi_exec_time)

    results[n_task] = result_table

# make dir for plot
if not os.path.exists(SAVE_DIR):
    os.makedirs(SAVE_DIR, exist_ok=True)

# helper for plotting
def plot(
    x: List[int],
    single_y: List[EXEC_TIME],
    multi_y: List[EXEC_TIME],
    xlabel: str,
    ylabel: str,
    title: str,
    save_name: str,
):
    """plot for single and multi processes execution time."""
    fig, ax = plt.subplots()

    ax.plot(x, single_y)
    ax.plot(x, multi_y)

    ax.set(xlabel=xlabel, ylabel=ylabel, title=title)
    ax.legend(["single", "multi"])
    ax.grid()

    fig.savefig(os.path.join(SAVE_DIR, save_name))
    plt.close()


print(results)
# plot
for n_task in N_TASKS:
    plot(
        x=N_ITERS,
        single_y=results[n_task]["single"],
        multi_y=results[n_task]["multi"],
        xlabel="Size of iteration",
        ylabel="Second",
        title=f"Single Process vs Multi Process with {n_task} tasks",
        save_name=f"task_{n_task}",
    )

for idx, n_iter in enumerate(N_ITERS):
    single_y: List[EXEC_TIME] = [results[n_task]["single"][idx] for n_task in N_TASKS]
    multi_y: List[EXEC_TIME] = [results[n_task]["multi"][idx] for n_task in N_TASKS]

    plot(
        x=N_TASKS,
        single_y=single_y,
        multi_y=multi_y,
        xlabel="Number of tasks",
        ylabel="Second",
        title=f"Single Process vs Multi Process with {n_iter} iteration",
        save_name=f"iteration_{n_iter}",
    )
