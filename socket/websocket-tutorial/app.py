#!/usr/bin/env python

import asyncio

import websockets


async def handler(websocket):
    async for message in websocket:  # Async Iteratio  # Async Iterationn
        print(message)


async def main():
    async with websockets.serve(
        ws_handler=handler,
        host="0.0.0.0",
        port=8001
    ):
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    asyncio.run(main())  # entry point of the program, create asyc io event loop

# websockets.serve()
# https://websockets.readthedocs.io/en/stable/reference/server.html#starting-a-server
# - ws_handler: client가 접근했을 때 connction을 관리하는 coroutine
#   - 입력 인자는 coroutine에게 전달된다.
#   - coroutine의 작업이 끝나면 websocket은 connection을 종료한다.
#   - handler가 infinite loop으로 되어 있어, 계속 살아있으면서 받는 message를 출력하게 된다.
# - host와 port: socket이 listen하는 network interface 정의

# websockets.serve의 첫 번째 인자: ws_handler
# - Callable로, 첫 입력 인자로 `websockets.legacy.server.WebSocketServerProtocol`을 받음
#   - https://websockets.readthedocs.io/en/stable/reference/server.html#using-a-connection 
# - asynchronous iteration 으로 사용 가능 -> `async for message in websocket` 가능
# - recv(), send() 등과 같은 coroutine 제공
