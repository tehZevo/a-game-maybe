from dataclasses import dataclass

from game.networking import RoomEventHandler

@dataclass
class WorldClosed:
  pass

class WorldClosedHandler(RoomEventHandler):
  def __init__(self, game):
    super().__init__(WorldClosed, game)

  def handle(self, event):
    print("[Client] Server closed world")
    self.game.transition()
