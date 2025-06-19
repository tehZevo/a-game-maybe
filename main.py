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
# TODO: doesnt work.. get:
#AttributeError: 'Lock' object has no attribute '_at_fork_reinit'
#at     reader, writer = await asyncio.open_connection(self.host, self.port)
# import game.run_web_networked

asyncio.run(main(scale_res=1))