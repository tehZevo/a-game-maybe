from dataclasses import dataclass

from ..event_handler import EventHandler
from game.tiles import Tileset

@dataclass
class TilesetUpdated:
  tileset: Tileset

class TilesetUpdatedHandler(EventHandler):
  def __init__(self):
    super().__init__(TilesetUpdated)

  def handle(self, client, event):
    print("received tileset", event)
