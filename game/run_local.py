import asyncio

from .client_game import ClientGame
from .server_game import ServerGame
from game.networking import LocalServer, LocalClient

async def main():
    server = LocalServer()
    client = LocalClient(server)
    server_game = ServerGame(server)
    client_game = ClientGame(client)
    
    await asyncio.gather(
        asyncio.create_task(server.start()),
        asyncio.create_task(client.connect()), #TODO: just await connect, no task
        asyncio.create_task(server_game.run()),
        asyncio.create_task(client_game.run())
    )

asyncio.run(main())