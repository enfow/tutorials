# Python Default Logger: Logging

## How to check the logging result

```bash
$ python run.py --func [function_name]
```

## Logging results example

1. There are 5 logging levels

```bash
$ python run.py --func five_log_levels
```

```bash
WARNING:root:This is warning
ERROR:root:This is error
CRITICAL:root:This is critical
```

2. User can set the log format

```bash
$ python run.py --func use_format
```

```bash
2021/04/04 12:35:43 [DEBUG] This is debug
2021/04/04 12:35:43 [INFO] This is info
2021/04/04 12:35:43 [WARNING] This is warning
2021/04/04 12:35:43 [ERROR] This is error
```
