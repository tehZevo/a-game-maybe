import math

import pygame

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
    #TODO: bake floors and render instead of individual sprites
    self.chunk_floors = {}

  def load_chunk(self, x, y, chunk):
    self.chunks[(x, y)] = chunk
    self.chunk_floors[(x, y)] = self.bake_chunk_floor(chunk)
  
  #TODO: ignoring floor height for now...
  def bake_chunk_floor(self, chunk):
    surface = pygame.Surface((CHUNK_SIZE * TILE_SIZE, CHUNK_SIZE * TILE_SIZE))
    for tx, ty, tile in chunk.itertiles():
      if tile.tile_type != TileType.FLOOR:
        continue
      image = get_image(self.mapdef.palette[tile.tile_type])
      surface.blit(image, (tx * TILE_SIZE, ty * TILE_SIZE))
    return surface
  
  def unload_chunk(self, x, y):
    if (x, y) not in self.chunks:
      print(f"[Client] Server asked us to unload already unloaded chunk at {x}, {y}")
      return
    del self.chunks[(x, y)]
    del self.chunk_floors[(x, y)]
  
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
      floor = self.chunk_floors[(cx, cy)]
      #TODO: not sure why there are black gaps
      renderer.draw(floor, Vector(cx * CHUNK_SIZE, cy * CHUNK_SIZE))

      for tx, ty, tile in chunk.itertiles():
        if tile.tile_type == TileType.EMPTY:# or tile.tile_type == TileType.FLOOR:
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
        renderer.draw(image, Vector(x, y), alpha=alpha, offset=Vector(0, -tile.y / 2))
