# /// script
# dependencies = [
#  "pygame",
#  "dacite",
# ]
# ///

import asyncio
import sys, platform
if sys.platform == "emscripten":
  platform.window.canvas.style.imageRendering = "pixelated"

#pygbag entrypoint
from game.run_client import main
from game.client_game import ClientMode

asyncio.run(main(ClientMode.WEB, scale_res=1))