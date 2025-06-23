from dataclasses import dataclass

from game.networking import RoomEventHandler

@dataclass
class WorldOpened:
  channel_id: str

class WorldOpenedHandler(RoomEventHandler):
  def __init__(self, game):
    super().__init__(WorldOpened, game)

  def handle(self, event):
    print("[Client] Server opened world")
    self.game.load_world(event.channel_id)
    
