from dataclasses import dataclass

from ..event_handler import EventHandler

@dataclass
class WorldOpened:
  pass

class WorldOpenedHandler(EventHandler):
  def __init__(self):
    super().__init__(WorldOpened)

  def handle(self, client_manager, client, event):
    from game.networking.commands import Sync
    print("[Client] Server opeened world")
    #TODO: without this, it seems we crash when loading a new map
    # - sync sent too quickly? seems to be related to mobs spawning?
    import time
    time.sleep(1)
    client.send(Sync())
