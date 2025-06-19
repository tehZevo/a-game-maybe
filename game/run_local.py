import asyncio

from .client_game import ClientGame
from .server_game import ServerGame
from game.networking import LocalServer, LocalClient

async def main(scale_res):
    server = LocalServer()
    client = LocalClient()
    server_game = ServerGame(server)
    client_game = ClientGame(client, scale_res=scale_res)
    
    await asyncio.gather(
        asyncio.create_task(server.start()),
        asyncio.create_task(client.connect(server)), #TODO: just await connect, no task
        asyncio.create_task(server_game.run()),
        asyncio.create_task(client_game.run())
    )

if __name__ == "__main__":
    asyncio.run(main(scale_res=3))