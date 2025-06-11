import pygame
from pygame.math import Vector2

from game.ecs import Component
from .drawable import Drawable
from game.components.physics import Position
from game.utils.image_cache import get_image
from game.utils.constants import PPU

#"bakes" tile images onto a surface for quicker blitting
class BakedTileset(Component, Drawable):
  def __init__(self, tileset):
    super().__init__()
    self.require(Position)
    self.tileset = tileset
    self.surface = None
    self.pos = None

  def start(self):
    self.pos = self.get_component(Position)
    self.surface = pygame.Surface((self.tileset.width * PPU, self.tileset.height * PPU))

    for x, y, tile in self.tileset.itertiles():
      self.bake(tile.image_path, x, y)

  def bake(self, path, x, y):
    if path is not None:
      image = get_image(path)
      self.surface.blit(image, (x * PPU, y * PPU))
  
  def draw(self, screen, offset):
    pos = self.pos.pos
    pos = Vector2(*(e * PPU for e in pos.tolist()))
    screen.blit(self.surface, pos + offset)
    
