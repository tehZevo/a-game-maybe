from dataclasses import dataclass

from ..event_handler import EventHandler
from game.tiles import Tileset

@dataclass
class TilesetUpdated:
  tileset: Tileset

class TilesetUpdatedHandler(EventHandler):
  def __init__(self):
    super().__init__(TilesetUpdated)

  def handle(self, client_manager, client, event):
    import game.components as C
    world = client_manager.entity.world
    world.create_entity([C.BakedTileset(event.tileset)])
    world.create_entity([C.TilesetPhysics(event.tileset)])
