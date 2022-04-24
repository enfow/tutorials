import asyncio
import websockets

async def say():
    async with websockets.connect("ws://localhost:8000/client") as websocket:
        while True:
            send_msg = input()
            await websocket.send(send_msg)
            recv_msg = await websocket.recv()
            print(recv_msg)

asyncio.run(say())
