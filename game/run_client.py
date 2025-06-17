import asyncio
from .client_game import ClientGame
from game.networking import WebsocketClient

URL = "ws://localhost:8765"

async def main():
    client = WebsocketClient("ws://localhost:8765")
    the_game = ClientGame(client)
    
    await asyncio.gather(
        asyncio.create_task(client.connect()),
        asyncio.create_task(the_game.run()),
    )

asyncio.run(main())