from dataclasses import dataclass

from ..event_handler import EventHandler
from game.tiles import Tileset, PackedTileset

@dataclass
class ChunkLoaded:
  x: int
  y: int
  tileset: PackedTileset

class ChunkLoadedHandler(EventHandler):
  def __init__(self):
    super().__init__(ChunkLoaded)

  def handle(self, client_manager, client, event):
    import game.components as C
    world = client_manager.entity.world
    #TODO: this is kinda expensive
    tile_rendering = world.find_component(C.TileRendering)
    tile_rendering.load_chunk(event.x, event.y, Tileset.unpack(event.tileset))
