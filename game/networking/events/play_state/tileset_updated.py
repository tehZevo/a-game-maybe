from dataclasses import dataclass

from game.networking import PlayStateEventHandler
from game.tiles import Tileset, PackedTileset
from game.data.registry import get_map

#TODO: rename or move the concept of setting mapdef's id on tilesetcomponent
#TODO: or could combine into "tilesupdated" with chunks to load and unload and mapdef...
@dataclass
class TilesetUpdated:
  map_id: str

class TilesetUpdatedHandler(PlayStateEventHandler):
  def __init__(self, game_state):
    super().__init__(TilesetUpdated, game_state)

  def handle(self, event):
    client_manager = self.game_state.client_manager
    import game.components as C
    world = client_manager.entity.world
    tile_rendering = world.find_component(C.TileRendering)
    tile_rendering.mapdef = get_map(event.map_id)
