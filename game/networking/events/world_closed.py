from dataclasses import dataclass

from ..event_handler import EventHandler

@dataclass
class WorldClosed:
  pass

class WorldClosedHandler(EventHandler):
  def __init__(self, client_game):
    super().__init__(WorldClosed)
    self.client_game = client_game

  def handle(self, client_manager, client, event):
    print("[Client] server says pool's closed")
    self.client_game.transition()
