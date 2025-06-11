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
    print("[Client] server says pool's open")
    #TODO: sleeping for dramatic effect
    import time
    time.sleep(1)
    client.send(Sync())
