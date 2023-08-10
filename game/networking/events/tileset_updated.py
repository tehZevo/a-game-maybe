from dataclasses import dataclass

from ..event_handler import EventHandler
from game.tiles import Tileset

@dataclass
class TilesetUpdated:
  tileset: Tileset

class TilesetUpdatedHandler(EventHandler):
  def __init__(self, client_manager):
    super().__init__(TilesetUpdated)
    self.client_manager = client_manager

  def handle(self, client, event):
    print(type(event.tileset))
