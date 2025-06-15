from dataclasses import dataclass

from ..event_handler import EventHandler

@dataclass
class ChunkUnloaded:
  x: int
  y: int

class ChunkUnloadedHandler(EventHandler):
  def __init__(self):
    super().__init__(ChunkUnloaded)

  def handle(self, client_manager, client, event):
    import game.components as C
    world = client_manager.entity.world
    #TODO: this is kinda expensive
    tile_rendering = world.find_component(C.TileRendering)
    tile_rendering.unload_chunk(event.x, event.y)
