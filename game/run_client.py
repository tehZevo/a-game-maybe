import asyncio
from .client_game import ClientGame, ClientMode

async def main(mode, scale_res=1):
  await ClientGame(mode, scale_res=scale_res).run()

if __name__ == "__main__":
  asyncio.run(main(ClientMode.DESKTOP, 4))