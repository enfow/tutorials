import asyncio
import websockets

async def pong(websocket):
    await websocket.send("Pong")

async def main():
    async with websockets.serve(pong, "localhost", 8765):
        await asyncio.Future()  # run forever

asyncio.run(main())

