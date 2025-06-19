import asyncio

from .client_game import ClientGame
from game.networking import JSWSClient

async def main():
    client = JSWSClient("ws://localhost:8765")
    the_game = ClientGame(client)
    
    await asyncio.gather(
        asyncio.create_task(client.connect()),
        asyncio.create_task(the_game.run()),
    )
