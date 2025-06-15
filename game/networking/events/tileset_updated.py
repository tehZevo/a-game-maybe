from dataclasses import dataclass

from ..event_handler import EventHandler
from game.tiles import Tileset, PackedTileset
from game.data.registry import get_map

#TODO: rename or move the concept of setting mapdef's id on tilesetcomponent
#TODO: or could combine into "tilesupdated" with chunks to load and unload and mapdef...
@dataclass
class TilesetUpdated:
  map_id: str

class TilesetUpdatedHandler(EventHandler):
  def __init__(self):
    super().__init__(TilesetUpdated)

  def handle(self, client_manager, client, event):
    import game.components as C
    world = client_manager.entity.world
    tile_rendering = world.find_component(C.TileRendering)
    tile_rendering.mapdef = get_map(event.map_id)
