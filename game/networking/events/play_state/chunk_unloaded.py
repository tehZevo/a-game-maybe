from dataclasses import dataclass

from game.networking import PlayStateEventHandler

@dataclass
class ChunkUnloaded:
  x: int
  y: int

class ChunkUnloadedHandler(PlayStateEventHandler):
  def __init__(self, game_state):
    super().__init__(ChunkUnloaded, game_state)

  def handle(self, event):
    import game.components as C
    world = self.game_state.client_manager.entity.world
    #TODO: this is kinda expensive
    tile_rendering = world.find_component(C.TileRendering)
    tile_rendering.unload_chunk(event.x, event.y)
