# Python Debugger: pdb

## Useful Command for pdb Prompter

### Basic Commands

- s(tep): go to next line
- n(ext): go to next line(same as step)
- c(ontinue): pass all lines until the breakpoint
- r(eturn): pass all lines until the return of the current function
- where : show current line
- l(ist): show source code of current function
- source [function_name]: show source code of the input function_name

### Source Code Level

- up: move the current frame count level up in the stack trace
- down: move the current frame count level down in the stack trace

### Break

- break [statement]: show breakpoints and it's number in the statement
- disable [breakpoint_number]: disable certain breakpoint
- enable [breakpoint_number]: enable certain breakpoint

- p [expression]: evaluate the expression with the current context

## Examples: pdb Prompter

### step(s), next(n), where, list

- Example with `$ python run.py`

```
> <string>(1)<module>()
(Pdb) step
--Call--
> /Users/woo/workspace/python_tutorials/pdb/run.py(32)example_function()
-> def example_function(value):
(Pdb) s
> /Users/woo/workspace/python_tutorials/pdb/run.py(34)example_function()
-> a = 10
(Pdb) n
> /Users/woo/workspace/python_tutorials/pdb/run.py(35)example_function()
-> b = 20
(Pdb) where
  /Users/woo/.pyenv/versions/3.8.2/lib/python3.8/bdb.py(580)run()
-> exec(cmd, globals, locals)
  <string>(1)<module>()
> /Users/woo/workspace/python_tutorials/pdb/run.py(35)example_function()
-> b = 20
(Pdb) list
 30
 31
 32     def example_function(value):
 33         """Define simple code example"""
 34         a = 10
 35  ->     b = 20
 36         c = 30
 37         return a + b + c + value
 38
 39
 40     if __name__ == "__main__":
(Pdb) continue

Press ENTER or type command to continue
```

### source, return

- Example with `$ python run.py`

```
> <string>(1)<module>()
(Pdb) source example_function
 32     def example_function(value):
 33         """Define simple code example"""
 34         a = 10
 35         b = 20
 36         c = 30
 37         return a + b + c + value
(Pdb) step
--Call--
> /Users/woo/workspace/python_tutorials/pdb/run.py(32)example_function()
-> def example_function(value):
(Pdb) step
> /Users/woo/workspace/python_tutorials/pdb/run.py(34)example_function()
-> a = 10
(Pdb) return
--Return--
> /Users/woo/workspace/python_tutorials/pdb/run.py(37)example_function()->70
-> return a + b + c + value
(Pdb) q

Press ENTER or type command to continue
```

### p, print()

- Example with `$ python run_breakpoint_example.py`

```
Press ENTER or type command to continue
> /Users/woo/workspace/python_tutorials/pdb/run_breakpoint_example.py(47)breakpoint_with_breakpoint()
-> c = 30
(Pdb) print(a)
10
(Pdb) p a
10
(Pdb) p a + b
30
(Pdb) where
  /Users/woo/workspace/python_tutorials/pdb/run_breakpoint_example.py(52)<module>()
-> breakpoint_with_breakpoint()
> /Users/woo/workspace/python_tutorials/pdb/run_breakpoint_example.py(47)breakpoint_with_breakpoint()
-> c = 30
(Pdb) p c
*** NameError: name 'c' is not defined
```
