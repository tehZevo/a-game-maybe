import asyncio

from .server_game import ServerGame
from game.networking import WebsocketServer

HOST = "localhost"
PORT = 8765

async def main():
    server = WebsocketServer(HOST, PORT)
    the_game = ServerGame(server)
    
    await asyncio.gather(
        asyncio.create_task(server.start()),
        asyncio.create_task(the_game.run()),
    )

asyncio.run(main())