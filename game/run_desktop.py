import asyncio
from .client_game import ClientGame, ClientMode

async def main():
    await ClientGame(ClientMode.DESKTOP, scale_res=3).run()
    
asyncio.run(main())