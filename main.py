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
from game.run_local import main
# from game.run_web_networked import main

asyncio.run(main(scale_res=1))