"""Compare multiprocess starting option: spawn and fork.

Author: Kyeongmin Woo
Email: wgm0601@gmail.com
"""
import os
import argparse
from typing import List
import time
import multiprocessing as mp

# type alias
EXEC_TIME = float
N_TASKS = mp.cpu_count()

parser = argparse.ArgumentParser()
parser.add_argument("--method", default="fork", type=str)
parser.add_argument("--trials", default=5, type=int)

args = parser.parse_args()
start_method = args.method

print(f"The start method is {start_method}")

def run_multi_process(start_method:str) -> EXEC_TIME:
    mp.set_start_method(start_method)
    start_p = time.time()
    with mp.Pool(N_TASKS) as p:
        p.map(time.sleep, [1 for _ in range(N_TASKS)])
    finish_p = time.time()
    return finish_p - start_p

if __name__ == "__main__":
    exec_times: List[EXEC_TIME] = list()
    exec_time = run_multi_process(start_method)
    exec_times.append(exec_time)

exec_avg = round(sum(exec_times) / len(exec_times), 5)
print(f"Average execution time: {exec_avg:10} sec")
    
