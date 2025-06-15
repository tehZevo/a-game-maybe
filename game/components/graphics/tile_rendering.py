import pygame
from pygame.math import Vector2

from game.ecs import Component
from .drawable import Drawable
import game.components as C
from game.utils.image_cache import get_image
from game.utils.constants import TILE_SIZE, CHUNK_SIZE
from game.utils import Vector

class TileRendering(Component, Drawable):
  def __init__(self):
    super().__init__()
    self.chunks = {}
    self.mapdef = None

  def load_chunk(self, x, y, chunk):
    self.chunks[(x, y)] = chunk
  
  def unload_chunk(self, x, y):
    if (x, y) not in self.chunks:
      print(f"[Client] Server asked us to unload already unloaded chunk at {x}, {y}")
      return
    del self.chunks[(x, y)]
  
  def draw(self, renderer):
    if self.mapdef is None:
      return
    for (cx, cy), chunk in self.chunks.items():
      for tx, ty, tile in chunk.itertiles():
        x = cx * CHUNK_SIZE + tx
        y = cy * CHUNK_SIZE + ty - tile.y / 2
        #TODO: draw with height
        #TODO: handle y-up :)
        image = get_image(self.mapdef.palette[tile.tile_type])
        renderer.draw(image, Vector(x, y))
