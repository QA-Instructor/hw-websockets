import asyncio
import websockets

async def hello(uri):
    async with websockets.connect(uri) as websocket:
        for x in range(10):
            await websocket.send("Hello world!")
            resp = await websocket.recv()
            print( resp )
        await websocket.send("quit")

asyncio.get_event_loop().run_until_complete(
    hello('ws://192.168.99.100:8765'))
