import pygame
from pygame.math import Vector2

from game.ecs import Component
from .drawable import Drawable
import game.components as C
from game.utils.image_cache import get_image
from game.utils.constants import TILE_SIZE
from game.utils import Vector

#"bakes" tile images onto a surface for quicker blitting
class BakedTileset(Component, Drawable):
  def __init__(self, tileset):
    super().__init__()
    self.require(C.Position)
    self.tileset = tileset
    self.surface = None
    self.pos = None
    self.mapdef = None

  def start(self):
    self.pos = self.get_component(C.Position)
    self.surface = pygame.Surface((self.tileset.width * TILE_SIZE, self.tileset.height * TILE_SIZE))
    self.mapdef = self.entity.world.find_component(C.GameMaster).mapdef
    for x, y, tile in self.tileset.itertiles():
      image_path = self.mapdef.palette[tile.tile_type]
      self.bake(image_path, x, y)

  def bake(self, path, x, y):
    if path is not None:
      image = get_image(path)
      print(image.get_size())
      self.surface.blit(image, (x * TILE_SIZE, y * TILE_SIZE))
  
  def draw_unbaked(self, renderer):
    #TODO: if this is fast enough, lets switch away from baking...
    #TODO: we may also be able to bake floors but not walls
    pos = self.pos.pos.copy()
    for x, y, tile in self.tileset.itertiles():
      #TODO: draw with height and y offset
      image_path = self.mapdef.palette[tile.tile_type]
      image = get_image(image_path)
      tile_offset = Vector(x, y - tile.y / 2) #TODO: handle y-up :)
      renderer.draw(image, pos + tile_offset)
    
  def draw(self, renderer):
    #TODO: reenable after refactoring rendering
    self.draw_unbaked(renderer)
    return 
    
    #TODO: surface is "too small" for tile bottoms...
    renderer.draw(self.surface, self.pos.pos.copy())
    
