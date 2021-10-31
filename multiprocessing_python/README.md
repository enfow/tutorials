# Python MultiProcessing Tutorial

## Contents

1. Compare single and multi process
1. Start method: Spawn and Fork 

## 1. compare single and multi process

- compare execution time of single process and multi processes with multi tasks
- [code](./01_compare_single_and_multi.py)

### How to run

```bash
[example]
$ python 01_compare_single_and_multi.py --n_iters 1000 10000 --n_tasks 1 2 3 4
```

## 2. start method: spawn and fork

- compare process start method: spawn and fork
- [code](./02_spawn_and_fork.py)


### How to run

```bash
$ python 02_spawn_and_fork.py -- method [spawn | fork]
```

### Spawn and Fork

- python multiprocessing has 3 process start method: spawn, fork and forkserve

#### Fork

- With `fork`, the child process inherits all of the resources of parents process.
- It is default for UNIX(without MacOS) and also available UNIX only.
- It looks more efficient but it should be considered unsafe(the reason why the macOS does not use fork as default).

```bash
$ python 02_spawn_and_fork.py --method fork
The start method is fork
Average execution time:    1.02497 sec  <- faster than spawn
```

#### Spawn
- With `spawn`, the parent process make a fresh python interpreter process.
- So it requires more time to make processes than fork's way.
- It is default for Windows(There are no fork in Window).

```bash
$ python 02_spawn_and_fork.py --method spawn
The start method is spawn
The start method is spawn
The start method is spawn
The start method is spawn
The start method is spawn
The start method is spawn
The start method is spawn
The start method is spawn
The start method is spawn
The start method is spawn
The start method is spawn
The start method is spawn
The start method is spawn
Average execution time:    2.02362 sec  <- slower than fork
```

- As you can see, all lines of the script runs many times with `spawn` option(line 25).
- So creating and running multiprocesses with `spawn` should be inside of the `if __name__ == "__main__"` clause. Otherwise, python raise the error as follows.

```bash
Traceback (most recent call last):
  File "<string>", line 1, in <module>
  File "/Users/pseudo_dir/.pyenv/versions/3.8.2/lib/python3.8/multiprocessing/spawn.py", line 116, in spawn_main
    exitcode = _main(fd, parent_sentinel)
  File "/Users/pseudo_dir/.pyenv/versions/3.8.2/lib/python3.8/multiprocessing/spawn.py", line 125, in _main
    prepare(preparation_data)
  File "/Users/pseudo_dir/.pyenv/versions/3.8.2/lib/python3.8/multiprocessing/spawn.py", line 236, in prepare
    _fixup_main_from_path(data['init_main_from_path'])
  File "/Users/pseudo_dir/.pyenv/versions/3.8.2/lib/python3.8/multiprocessing/spawn.py", line 287, in _fixup_main_from_path
    main_content = runpy.run_path(main_path,
  File "/Users/pseudo_dir/.pyenv/versions/3.8.2/lib/python3.8/runpy.py", line 263, in run_path
    return _run_module_code(code, init_globals, run_name,
  File "/Users/pseudo_dir/.pyenv/versions/3.8.2/lib/python3.8/runpy.py", line 96, in _run_module_code
    _run_code(code, mod_globals, init_globals,
  File "/Users/pseudo_dir/.pyenv/versions/3.8.2/lib/python3.8/runpy.py", line 86, in _run_code
    exec(code, run_globals)
  File "/Users/pseudo_dir/workspace/tutorials/multiprocessing_python/02_spawn_and_fork.py", line 37, in <module>
    exec_time = run_multi_process(start_method)
  File "/Users/pseudo_dir/workspace/tutorials/multiprocessing_python/02_spawn_and_fork.py", line 28, in run_multi_process
    mp.set_start_method(start_method)
  File "/Users/pseudo_dir/.pyenv/versions/3.8.2/lib/python3.8/multiprocessing/context.py", line 243, in set_start_method
    raise RuntimeError('context has already been set')
RuntimeError: context has already been set
```

### tips:

- How to select the start method: `mp.set_start_method()`

```python
mp.set_start_method('spawn')
```

- `mp.set_start_method()` should net be used more than once in the program.

## References

- [Python Docs](<https://docs.python.org/3/library/multiprocessing.html>)
