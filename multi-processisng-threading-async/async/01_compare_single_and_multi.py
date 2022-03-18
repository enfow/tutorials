"""Compare with sync and asyc.

Author: Kyeongmin Woo
Email: wgm0601@gmail.com
"""

import os
import argparse
from typing import Dict, List
import time
import asyncio

import matplotlib.pyplot as plt

# type alias`
N_ITER = int
N_TASK = int
EXEC_TIME = float
RESULTS = Dict[N_TASK, Dict[str, List[EXEC_TIME]]]

# argment parser
parser = argparse.ArgumentParser()
parser.add_argument("--seconds", nargs="+", default=[3], type=int)
parser.add_argument("--n_tasks", nargs="+", default=[1, 2, 3, 4, 5, 6, 7, 8], type=int)
args = parser.parse_args()

# global variables
SAVE_DIR = os.path.join("img", "compare_single_and_multi")
SECS = args.seconds
N_TASKS = args.n_tasks

# task
async def async_sleep(sec: int = 3) -> None:
    """Run double for iteration."""
    await asyncio.sleep(sec)

def sync_sleep(sec: int = 3) -> None:
    """Run double for iteration."""
    time.sleep(sec)


async def main():

    results: RESULTS = dict()
    for n_task in N_TASKS:

        result_table: Dict[str, List[EXEC_TIME]] = {
            "async": list(),
            "sync": list(),
        }

        for sec in SECS:

            # multi threading
            start_time = time.time()

            task_set = [
                asyncio.create_task(async_sleep(sec))
                for _ in range(n_task)
            ]
            
            for task in task_set:
                await task

            end_time = time.time()

            result_table["async"].append(end_time - start_time)

            # single threading
            start_time = time.time()

            for task in range(n_task):
                sync_sleep(sec)

            end_time = time.time()

            result_table["sync"].append(end_time - start_time)

        results[n_task] = result_table

    return results


results = asyncio.run(main())


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
    """plot for single and multi thread execution time."""
    fig, ax = plt.subplots()

    ax.plot(x, single_y)
    ax.plot(x, multi_y)

    ax.set(xlabel=xlabel, ylabel=ylabel, title=title)
    ax.legend(["sync", "async"])
    ax.grid()

    fig.savefig(os.path.join(SAVE_DIR, save_name))
    plt.close()


print(results)
# plot
for n_task in N_TASKS:
    plot(
        x=SECS,
        single_y=results[n_task]["sync"],
        multi_y=results[n_task]["async"],
        xlabel="sec per task",
        ylabel="Second",
        title=f"Sync vs Async with {n_task} tasks",
        save_name=f"task_{n_task}",
    )

for idx, sec in enumerate(SECS):
    single_y: List[EXEC_TIME] = [results[n_task]["sync"][idx] for n_task in N_TASKS]
    multi_y: List[EXEC_TIME] = [results[n_task]["async"][idx] for n_task in N_TASKS]

    plot(
        x=N_TASKS,
        single_y=single_y,
        multi_y=multi_y,
        xlabel="Number of tasks",
        ylabel="Second",
        title=f"Sync vs Async with {sec} sec per task",
        save_name=f"sec_{sec}",
    )
