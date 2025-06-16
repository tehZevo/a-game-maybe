import math

import pygame
from pygame.math import Vector2

from game.ecs import Component
from .drawable import Drawable
import game.components as C
from game.utils.image_cache import get_image
from game.utils.constants import TILE_SIZE, CHUNK_SIZE
from game.utils import Vector
from game.tiles import TileType

def is_behind(px, py, tx, ty):
  if px > tx - 1 and px < tx + 1 and py < ty and py > ty - 1.5:
    return True
  return False

class TileRendering(Component, Drawable):
  def __init__(self):
    super().__init__()
    self.chunks = {}
    self.mapdef = None
    self.player = None

  def load_chunk(self, x, y, chunk):
    self.chunks[(x, y)] = chunk
  
  def unload_chunk(self, x, y):
    if (x, y) not in self.chunks:
      print(f"[Client] Server asked us to unload already unloaded chunk at {x}, {y}")
      return
    del self.chunks[(x, y)]
  
  def draw(self, renderer):
    #TODO: wat
    if self.mapdef is None:
      return
    if self.player is None:
      pc = self.entity.world.find_component(C.PlayerController)
      if pc is not None:
        self.player = pc.player
    if self.player is None:
      return
    
    player_pos = self.player.get_component(C.Position).pos
    
    for (cx, cy), chunk in list(self.chunks.items()).copy():
      for tx, ty, tile in chunk.itertiles():
        if tile.tile_type == TileType.EMPTY:
          continue
        x = cx * CHUNK_SIZE + tx
        y = cy * CHUNK_SIZE + ty
        #TODO: draw with height
        #TODO: handle y-up :)
        image = get_image(self.mapdef.palette[tile.tile_type])
        if tile.tile_type == TileType.WALL and is_behind(player_pos.x, player_pos.y, x, y):
          alpha = 0.5
        else:
          alpha = 1
        renderer.draw(image, Vector(x, y - tile.y / 2), alpha=alpha)
