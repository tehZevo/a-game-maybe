import asyncio
from .client_game import ClientGame
from game.networking import WebsocketClient
from game.networking import StreamClient

HOST = "127.0.0.1"
PORT = 8765
URL = f"ws://{HOST}:{PORT}"

async def main():
    client = WebsocketClient(URL)
    # client = StreamClient(HOST, PORT)
    the_game = ClientGame(client, scale_res=3)
    
    await asyncio.gather(
        asyncio.create_task(client.connect()),
        asyncio.create_task(the_game.run()),
    )

asyncio.run(main())