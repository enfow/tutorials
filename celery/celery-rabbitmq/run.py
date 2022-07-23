import tasks


sleep_result = tasks.sleep_three.delay()
add_result = tasks.add.delay(1,2)


sleep_printed, add_printed = False, False

while not sleep_printed or not add_printed:
    if sleep_result.ready() and not sleep_printed:
        print(f"sleep_result: {sleep_result.get()}")
        sleep_printed = True
    if add_result.ready() and not add_printed:
        print(f"add_result: {add_result.get()}")
        add_printed = True

"""
$ python run.py
add_result: 3
sleep_result: True

### Celery Log ###
[2022-07-22 13:33:27,954: INFO/MainProcess] Task tasks.sleep_three[a1d984d7-de99-4059-8521-f43a1b62be48] received
[2022-07-22 13:33:27,957: INFO/MainProcess] Task tasks.add[7b104039-2ba3-4aa4-9161-f2a5de67960a] received
[2022-07-22 13:33:27,973: INFO/ForkPoolWorker-1] Task tasks.add[7b104039-2ba3-4aa4-9161-f2a5de67960a] succeeded in 0.01475167899999974s: 3
[2022-07-22 13:33:30,968: INFO/ForkPoolWorker-8] Task tasks.sleep_three[a1d984d7-de99-4059-8521-f43a1b62be48] succeeded in 3.0128888209999998s: True
"""
