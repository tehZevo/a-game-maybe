from dataclasses import dataclass

from game.networking import PlayStateEventHandler
from game.tiles import Tileset, PackedTileset

@dataclass
class ChunkLoaded:
  x: int
  y: int
  tileset: PackedTileset

class ChunkLoadedHandler(PlayStateEventHandler):
  def __init__(self, game_state):
    super().__init__(ChunkLoaded, game_state)

  def handle(self, event):
    import game.components as C
    world = self.game_state.client_manager.entity.world
    tile_rendering = world.find_component(C.TileRendering)
    tile_phys = world.find_component(C.TilePhysics)
    chunk = Tileset.unpack(event.tileset)
    tile_rendering.load_chunk(event.x, event.y, chunk)
    tile_phys.load_chunk(event.x, event.y, chunk)
